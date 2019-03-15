from .mapper import *
# Internal
from src.common.decorators import override
from src.helper.interval import Unit, Interval
from src.domain.objects.session import Session
from src.domain.converters.date_time_converter import DateTimeConverter


class SessionMapper(Mapper):

    def findAll(self):

        dataSets = self.abstractFind('SELECT * FROM SessionView')

        sessions = self.handleDataSets(dataSets)
        return sessions


    def findInsideTimestamp(self, *, interval: Interval, inclusive = False):

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
