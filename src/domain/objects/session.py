from .database_object import *


class Session(DatabaseObject):

    def __init__(self):
        super().__init__()

        self.unit: float = None

        self.startUtcTime: str = None
        self.stopUtcTime: str = None


    def __eq__(self, other):

        return all((self.unit == other.unit,
                    self.startUtcTime == other.startUtcTime,
                    self.stopUtcTime == other.stopUtcTime))


    def toDict(self):

        return \
        {
            'primaryKey': self.primaryKey,
            'startUtcTime': self.startUtcTime,
            'stopUtcTime': self.stopUtcTime
        }
