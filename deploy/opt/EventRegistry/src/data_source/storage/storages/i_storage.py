# Internal
from src.helper.interval import Interval


class IStorage:

    def findAllSessions(self):
        raise NotImplementedError


    def findSessionsInsideTimestamp(self, includeIncompleteEntries: bool, interval: Interval):
        raise NotImplementedError


    def findAllPipes(self):
        raise NotImplementedError


    def findPipesForSessions(self, sessionsId: list):
        raise NotImplementedError


    def findRecordsForPipe(self, pipeId: int, interval: Interval = None):
        raise NotADirectoryError
