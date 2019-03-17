from .mapper import *
# Internal
from src.domain.objects.record import Record
from src.helper.interval import Unit, Interval
from src.common.decorators import override, private
from src.domain.converters.date_time_converter import DateTimeConverter
from src.domain.mavlink.mavlink_package_generator import MavlinkPackageGenerator


class RecordMapper(Mapper):

    def __init__(self, dbConnection):
        super().__init__(dbConnection)

        self.metadata: str = None

        self.mavlinkGenerator = MavlinkPackageGenerator()


    def findRecordsForPipe(self, pipeId, interval: Interval = None):

        if interval:

            interval = interval.transformTo(Unit.Second)
            dataSets = self.abstractFind('SELECT * FROM RecordView WHERE PipeId = ? '
                                    'AND RecordTimeInSec >= ? AND  RecordTimeInSec <= ?', (pipeId, interval.start, interval.stop))
        else:
            dataSets = self.abstractFind('SELECT * FROM RecordView WHERE PipeId = ?', (pipeId, ))


        records = self.handleDataSets(dataSets)
        return records


    def createRecordView(self):

        createRecordView = """CREATE VIEW RecordView AS SELECT r.Id, r.PipeId, 
        strftime('%s', strftime('%Y-%m-%d %H:%M',s.OriginTime, 'utc')) + 
        strftime('%f',s.OriginTime) + s.Unit * (r.Timestamp - s.Timestamp) as RecordTimeInSec,
        r.SerialData 
        FROM Session s, Pipe p, Record r WHERE p.SessionId = s.Id AND r.PipeId = p.Id ORDER BY r.Timestamp;"""
        self.dbConnection.execute(createRecordView)
        self.dbConnection.commit()



    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        record = Record()
        record.primaryKey = next(iterator)

        record.pipeId = next(iterator)
        record.utcTime = DateTimeConverter.translateSecondsSinceEpochToUtc(next(iterator))

        serialData = next(iterator)
        # TODO: property
        self.mavlinkGenerator.changeDialect(self.metadata)
        record.package = self.mavlinkGenerator.generatePackageFor(serialData)

        return record
