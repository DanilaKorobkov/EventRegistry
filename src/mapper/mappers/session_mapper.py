from .mapper import *
# Internal
from src.common.decorators import override
from src.helper.interval import Unit, Interval
from src.domain.objects.session import Session
from src.domain.converters.date_time_converter import DateTimeConverter


class SessionMapper(Mapper):

    def findAll(self):

        self.createSessionView()

        dataSets = self.abstractFind('SELECT * FROM SessionView')

        sessions = self.handleDataSets(dataSets)
        return sessions


    def findInsideTimestamp(self, *, interval: Interval, inclusive = False):

        self.createSessionView()

        interval = interval.transformTo(Unit.Second)

        if inclusive:
            dataSets = self.abstractFind('SELECT * FROM SessionView WHERE (StartSession >= ? and StartSession <= ?) '
                                         'or (EndSession >= ? and EndSession <= ?)',
                                         (interval.start, interval.stop, interval.start, interval.stop))

        else:
            dataSets = self.abstractFind('SELECT * FROM SessionView WHERE StartSession >= ? and EndSession <= ?',
                                         (interval.start, interval.stop))

        sessions = self.handleDataSets(dataSets)
        return sessions

    def createSessionView(self):

        dropView = 'DROP VIEW IF EXISTS SessionView'
        self.dbConnection.execute(dropView)

        createSessionView = """CREATE VIEW SessionView AS 
        SELECT s.Id,
        strftime('%s', strftime('%Y-%m-%d %H:%M',s.OriginTime, 'utc')) + strftime('%f',s.OriginTime) as StartSession,
        strftime('%s', strftime('%Y-%m-%d %H:%M',s.OriginTime, 'utc')) + strftime('%f',s.OriginTime) + 
        s.Unit * (s2.EndSession - s.Timestamp) as EndSession, 
        s.OriginTime 
        FROM Session s, (SELECT s.Id, s.Timestamp, MAX(r.Timestamp) as EndSession FROM Record r, Pipe p, Session s 
        WHERE s.Id = p.SessionId AND p.Id = r.PipeId GROUP BY s.Id) s2 WHERE s.Id = s2.Id ORDER BY s.OriginTime"""
        self.dbConnection.execute(createSessionView)

        self.dbConnection.commit()




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
