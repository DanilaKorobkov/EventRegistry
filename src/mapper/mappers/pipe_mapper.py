from .mapper import *
# Internal
from src.common.decorators import override
from src.domain.objects.pipe import Pipe


class PipeMapper(Mapper):

    def findAll(self):

        dataSets = self.abstractFind('SELECT * FROM Pipe')
        return self.handleDataSets(dataSets)


    def findPipesForSessions(self, sessionsId):

        searchRange = str(tuple(sessionsId))

        if len(sessionsId) == 1:
            searchRange = searchRange.replace(',', '')

        dataSets = self.abstractFind('SELECT * FROM Pipe WHERE SessionId IN {0}'.format(searchRange))

        pipes = self.handleDataSets(dataSets)
        return pipes


    @override
    def handleDataSet(self, dataSet):

        iterator = iter(dataSet)

        pipe = Pipe()

        pipe.primaryKey = next(iterator)
        pipe.sessionId = next(iterator)
        pipe.path = next(iterator).decode('utf-8').split('/')[1: -1]
        pipe.metaData = next(iterator).decode('utf-8')

        return pipe
