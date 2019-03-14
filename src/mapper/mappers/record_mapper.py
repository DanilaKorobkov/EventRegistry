from .mapper import *
# Internal
from src.domain.objects.record import Record
from src.common.decorators import override, private
from src.domain.converters.date_time_converter import DateTimeConverter
from src.domain.mavlink.mavlink_package_generator import MavlinkPackageGenerator


class RecordMapper(Mapper):

    def __init__(self, dbConnection):
        super().__init__(dbConnection)

        self.metadata: str = None

        self.mavlinkGenerator = MavlinkPackageGenerator()

        self.sessionUnit: float = None
        self.sessionTimestamp: int = None
        self.sessionStartTime: str = None


    def findRecordsForPipe(self, pipeId):

        dataSet = self.abstractFind('SELECT Timestamp, Unit, OriginTime FROM Session s, Pipe p '
                                    'WHERE s.Id = p.SessionId AND p.Id = ?', (pipeId, ))
        self.handleSessionDataSet(dataSet)

        dataSets = self.abstractFind('SELECT * FROM Record WHERE PipeId = ?', (pipeId, ))
        records = self.handleDataSets(dataSets)
        return records


    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        record = Record()

        record.primaryKey = next(iterator)
        record.pipeId = next(iterator)

        timeStamp = next(iterator)

        recordsClockTime = self.sessionTimestamp - timeStamp
        recordsSecondsTime = recordsClockTime * self.sessionUnit
        sessionStartSecondsSinceEpoch = DateTimeConverter.translateUtcToSecondsSinceEpoch(self.sessionStartTime)

        record.utcTime = DateTimeConverter.translateSecondsSinceEpochToUtc(sessionStartSecondsSinceEpoch+ recordsSecondsTime)

        serialData = next(iterator)

        self.mavlinkGenerator.changeDialect(self.metadata)

        record.package = self.mavlinkGenerator.generatePackageFor(serialData)

        return record

    @private
    def handleSessionDataSet(self, dataSet):

        dataSet = dataSet.fetchall()[0]

        self.sessionTimestamp, self.sessionUnit, self.sessionStartTime = dataSet
        self.sessionStartTime = self.sessionStartTime.decode('utf-8')

        self.sessionStartTime = DateTimeConverter.dropUtcNanoseconds(self.sessionStartTime)
