from .database_object import *
# Internal
from src.helper.time_point import  TimePoint, Unit
from src.domain.wrappers.i_package_wrapper import IPackageWrapper


class Record(DatabaseObject):

    def __init__(self):
        super().__init__()

        self.pipeId = None
        self.timePoint = None
        self.package = None


    def __eq__(self, other):

        return all((self.pipeId == other.pipeId,
                    self.timePoint == other.timePoint,
                    self.package == other.package))


    def toDict(self):

        dictionary = \
        {
            'primaryKey': self.primaryKey,
            'utcTime': self.timePoint.transformTo(Unit.Utc).value,
            'fields': self.package.toDict()
        }

        return dictionary