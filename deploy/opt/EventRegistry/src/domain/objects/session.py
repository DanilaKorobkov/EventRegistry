from .database_object import *
# Internal
from src.helper.interval import Interval, Unit


class Session(DatabaseObject):

    def __init__(self):
        super().__init__()

        self.interval = None


    def __eq__(self, other):

        return self.interval == other.interval


    def toDict(self):

        utcInterval = self.interval.transformTo(Unit.Utc)

        return \
        {
            'primaryKey': self.primaryKey,
            'startUtcTime': utcInterval.start.value,
            'stopUtcTime': utcInterval.stop.value
        }
