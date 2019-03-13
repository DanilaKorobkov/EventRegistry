from .database_object import *
# Internal
from src.domain.wrappers.i_package_wrapper import IPackageWrapper


class Record(DatabaseObject):

    def __init__(self):
        super().__init__()

        self.pipeId: int = None
        self.utcTime: str = None
        self.package: IPackageWrapper = None


    def __eq__(self, other):
        return all((self.pipeId == other.pipeId, self.utcTime == other.utcTime, self.package == other.package))


    def toDict(self):

        dictionary = \
        {
            'primaryKey': self.primaryKey,
            'utcTime': self.utcTime,
            'fields': self.package.toDict()
        }

        return dictionary