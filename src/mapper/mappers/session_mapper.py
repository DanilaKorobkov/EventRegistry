from .mapper import *
# Internal
from src.common.decorators import override
from src.domain.objects.session import Session
from src.domain.converters.date_time_converter import DateTimeConverter


class SessionMapper(Mapper):

    def findAll(self):

        dataSets = self.abstractFind('SELECT s1.Id, s1.Timestamp, s2.EndSession, s1.Unit, s1.OriginTime FROM Session s1,'
                              '(SELECT s.Id, s.Timestamp, MAX(r.Timestamp) as EndSession FROM Record r, Pipe p, Session s '
                              'WHERE s.Id = p.SessionId AND p.Id = r.PipeId GROUP BY s.Id) s2 WHERE s1.Id = s2.Id')

        sessions = self.handleDataSets(dataSets)
        return sessions


    def filterSessions(self, sessions: iter, start, stop, inclusive):

        result = []

        start = DateTimeConverter.translateUtcToSecondsSinceEpoch(start)
        stop = DateTimeConverter.translateUtcToSecondsSinceEpoch(stop)

        for session in sessions:

            sessionStart = DateTimeConverter.translateUtcToSecondsSinceEpoch(session.startUtcTime)
            sessionStop = DateTimeConverter.translateUtcToSecondsSinceEpoch(session.stopUtcTime)

            if inclusive:

                if (sessionStart >= start and sessionStart <= stop) or (sessionStop >= start and sessionStop <= stop):
                    result.append(session)

            else:
                if sessionStart >= start and sessionStop <= stop:

                    result.append(session)


        return result




    def findInsideTimestamp(self, *, start, stop, inclusive = False):

        sessions = self.findAll()
        sessions = self.filterSessions(sessions, start, stop, inclusive)
        return sessions

        # if not inclusive:
        #
        #     dataSets = self.abstractFind('SELECT s1.Id, s1.Timestamp, s2.EndSession, s1.Unit, s1.OriginTime FROM Session s1,'
        #                       '(SELECT s.Id, s.Timestamp, MAX(r.Timestamp) as EndSession FROM Record r, Pipe p, Session s '
        #                       'WHERE s.Id = p.SessionId AND p.Id = r.PipeId GROUP BY s.Id) s2 '
        #                       'WHERE s1.Id = s2.Id AND s2.Timestamp >= ? AND s2.EndSession <= ?', (start, stop))
        # else:
        #
        #     dataSets = self.abstractFind('SELECT s1.Id, s1.Timestamp, s2.EndSession, s1.Unit, s1.OriginTime FROM Session s1, '
        #                       '(SELECT s.Id, s.Timestamp, MAX(r.Timestamp) as EndSession FROM Record r, Pipe p, Session s '
        #                       'WHERE s.Id = p.SessionId AND p.Id = r.PipeId GROUP BY s.Id) s2 '
        #                       'WHERE s1.Id = s2.Id AND ((? BETWEEN s2.Timestamp AND s2.EndSession) '
        #                       'OR (? BETWEEN s2.Timestamp AND s2.EndSession))', (start, stop))
        #
        # return self.handleDataSets(dataSets)


    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        session = Session()
        session.primaryKey = next(iterator)


        startTimestamp = next(iterator)
        stopTimestamp = next(iterator)

        session.unit = next(iterator)

        startOriginTime = next(iterator).decode('utf-8')
        session.startUtcTime = DateTimeConverter.dropUtcNanoseconds(startOriginTime)

        sessionClocksDuration = stopTimestamp - startTimestamp
        sessionSecondsDuration = sessionClocksDuration * session.unit
        sessionStartSecondsSinceEpoch = DateTimeConverter.translateUtcToSecondsSinceEpoch(session.startUtcTime)

        session.stopUtcTime = DateTimeConverter.translateSecondsSinceEpochToUtc(sessionStartSecondsSinceEpoch + sessionSecondsDuration)

        return session
