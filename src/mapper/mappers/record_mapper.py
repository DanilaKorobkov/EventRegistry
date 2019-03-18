from .mapper import *
# Internal
from src.domain.objects.record import Record
from src.helper.interval import Unit, Interval
from src.common.decorators import override, private
from src.domain.converters.date_time_converter import DateTimeConverter
from src.domain.mavlink.mavlink_package_generator import MavlinkPackageGenerator
from src.helper.time_point import Unit, TimePoint

class RecordMapper(Mapper):

    def __init__(self, dbConnection):
        super().__init__(dbConnection)

        self.__mavlinkGenerator = MavlinkPackageGenerator()
        self.__metaData: str = None


    @property
    def metaData(self):

        return self.__metaData


    @metaData.setter
    def metaData(self, metaData):

        if self.metaData != metaData:

            self.__metaData = metaData
            self.__mavlinkGenerator.changeDialect(self.metaData)


    def findRecordsForPipe(self, pipeId, interval: Interval = None):

        if interval:

            interval = interval.transformTo(Unit.Second)
            dataSets = self.abstractFind('SELECT * FROM RecordView WHERE PipeId = ? '
                                    'AND RecordTimeInSec >= ? AND  RecordTimeInSec <= ?', (pipeId,
                                                                                           interval.start.value,
                                                                                           interval.stop.value))
        else:
            dataSets = self.abstractFind('SELECT * FROM RecordView WHERE PipeId = ?', (pipeId, ))


        records = self.handleDataSets(dataSets)
        return records


    def createRecordView(self):

        dropView = 'DROP VIEW IF EXISTS RecordView'
        self.dbConnection.execute(dropView)

        sessionStartSec = "strftime('%s', strftime('%Y-%m-%d %H:%M',s.OriginTime, 'utc')) + strftime('%f',s.OriginTime)"
        recordSecFromSessionStart = sessionStartSec + ' + ' + "s.Unit * (r.Timestamp - s.Timestamp)"

        createRecordView = """CREATE VIEW RecordView AS SELECT r.Id, r.PipeId, 
                           {RecordTimeInSec} as RecordTimeInSec, r.SerialData 
                           FROM Session s, Pipe p, Record r 
                           WHERE p.SessionId = s.Id AND r.PipeId = p.Id 
                           ORDER BY r.Timestamp;""".format(RecordTimeInSec = recordSecFromSessionStart)

        self.dbConnection.execute(createRecordView)
        self.dbConnection.commit()



    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        record = Record()
        record.primaryKey = next(iterator)

        record.pipeId = next(iterator)

        recordTimeInSeconds = next(iterator)
        record.timePoint = TimePoint(recordTimeInSeconds, Unit.Second)

        serialData = next(iterator)
        record.package = self.__mavlinkGenerator.generatePackageFor(serialData)

        return record
