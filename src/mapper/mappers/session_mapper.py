from .mapper import *
# Internal
from src.common.decorators import override
from src.helper.interval import Unit, Interval
from src.domain.objects.session import Session
from src.domain.converters.date_time_converter import DateTimeConverter


def findSessionWrapper(func):

    def Impl(*args, **kwargs):

        self = args[0]
        self.createSessionView()

        data = func(*args, **kwargs)

        result = self.handleDataSets(data)
        return result

    return Impl


class SessionMapper(Mapper):

    @findSessionWrapper
    def findAll(self):

        dataSets = self.abstractFind('SELECT * FROM SessionView')
        return dataSets


    @findSessionWrapper
    def findInsideTimestamp(self, *, interval: Interval, inclusive = False):

        interval = interval.transformTo(Unit.Second)

        if inclusive:
            dataSets = self.abstractFind('SELECT * FROM SessionView WHERE (StartSession >= ? and StartSession <= ?) '
                                         'or (EndSession >= ? and EndSession <= ?)',
                                         (interval.start, interval.stop, interval.start, interval.stop))

        else:
            dataSets = self.abstractFind('SELECT * FROM SessionView WHERE StartSession >= ? and EndSession <= ?',
                                         (interval.start, interval.stop))

        return dataSets


    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        session = Session()
        session.primaryKey = next(iterator)

        sessionStartInSeconds = next(iterator)
        sessionStopInSeconds = next(iterator)

        session.startUtcTime = DateTimeConverter.translateSecondsSinceEpochToUtc(sessionStartInSeconds)
        session.stopUtcTime = DateTimeConverter.translateSecondsSinceEpochToUtc(sessionStopInSeconds)

        return session


    def createSessionView(self):

        dropView = 'DROP VIEW IF EXISTS SessionView'
        self.dbConnection.execute(dropView)

        sessionStartSec = "strftime('%s', strftime('%Y-%m-%d %H:%M',s.OriginTime, 'utc')) + strftime('%f',s.OriginTime)"
        recordSecFromSessionStart = sessionStartSec + ' + ' + "s.Unit * (s2.EndSession - s.Timestamp)"
        sessionMaxRecordTable = """(SELECT s.Id, s.Timestamp, MAX(r.Timestamp) as EndSession 
                                FROM Record r, Pipe p, Session s
                                WHERE s.Id = p.SessionId AND p.Id = r.PipeId GROUP BY s.Id)"""


        createSessionView = """CREATE VIEW SessionView AS SELECT s.Id, {StartSession} as StartSession, 
                            {RecordTime} as EndSession, s.OriginTime FROM Session s, {SessionMaxRecordTable} s2 
                            WHERE s.Id = s2.Id ORDER BY s.OriginTime""".format(StartSession = sessionStartSec,
                                                                               RecordTime = recordSecFromSessionStart,
                                                                               SessionMaxRecordTable = sessionMaxRecordTable)
        self.dbConnection.execute(createSessionView)
        self.dbConnection.commit()
