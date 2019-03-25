from .database_object import *


class Pipe(DatabaseObject):

    def __init__(self):
        super().__init__()

        self.sessionId = None

        self.path = None
        self.metaData = None


    def __eq__(self, other):

        return all((self.sessionId == other.sessionId,
                    self.path == other.path,
                    self.metaData == other.metaData))


    def toDict(self):

        dictionary = \
            {
                'primaryKey': self.primaryKey,
                'path': self.path
            }

        return dictionary