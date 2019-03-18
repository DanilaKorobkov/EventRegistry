from .mapper import *
# Internal
from src.helper.interval import Interval
from src.common.decorators import override
from src.domain.objects.session import Session
from src.helper.time_point import TimePoint, Unit


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
    def findInsideTimestamp(self, includeIncompleteEntries, interval: Interval):

        interval = interval.transformTo(Unit.Second)

        if includeIncompleteEntries:
            dataSets = self.abstractFind('SELECT * FROM SessionView WHERE (StartSession >= ? and StartSession <= ?) '
                                         'or (EndSession >= ? and EndSession <= ?)',
                                         (interval.start.value, interval.stop.value, interval.start.value, interval.stop.value))

        else:
            dataSets = self.abstractFind('SELECT * FROM SessionView WHERE StartSession >= ? and EndSession <= ?',
                                         (interval.start.value, interval.stop.value))

        return dataSets


    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        session = Session()
        session.primaryKey = next(iterator)

        sessionStartInSeconds = next(iterator)
        sessionStopInSeconds = next(iterator)

        session.interval = Interval(TimePoint(sessionStartInSeconds, Unit.Second),
                                    TimePoint(sessionStopInSeconds, Unit.Second))

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
