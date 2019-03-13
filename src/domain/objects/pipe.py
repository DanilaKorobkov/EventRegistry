from .database_object import *


class Pipe(DatabaseObject):

    def __init__(self):
        super().__init__()

        self.sessionId: int = None

        self.path: list = None
        self.metaData: bytes = None

        self.records = []


    def __eq__(self, other):

        return all((self.sessionId == other.sessionId, self.path == other.path,
                    self.metaData == other.metaData, self.records == other.records))


    def toDict(self):

        dictionary = \
            {
                'primaryKey': self.primaryKey,
                'path': self.path
            }

        if self.records:

            records = [record.toDict() for record in self.records]
            dictionary.update({'records': records})

        return dictionary