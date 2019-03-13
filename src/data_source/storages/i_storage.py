

class IStorage:

    def findAllSessions(self):
        raise NotImplementedError


    def findSessionsInsideTimestamp(self, parameters: dict):
        raise NotImplementedError


    def findAllPipes(self, includeRecords: bool):
        raise NotImplementedError


    def findPipesForSessions(self, sessionsId: list, includeRecords: bool):
        raise NotImplementedError