from .i_request_handler import *
# Internal
from src.helper.interval import Interval
from src.common.decorators import private
from src.helper.time_point import Unit, TimePoint
from src.helper.request_wrapper import RequestWrapper


class ReadRequestHandler(IRequestHandler):

    def handle(self, request: RequestWrapper):

        if request.get('what') == 'Pipes':
            return self.handlePipesRequest(request)

        if request.get('what') == 'Sessions':
            return self.handleSessionsRequest(request)

        if request.get('what') == 'Records':
            return self.handleRecordsRequest(request)



    def handleSessionsRequest(self, request: RequestWrapper):

        if request.getAllParameters() == {'what'}:
            sessions = self.storage.findAllSessions()

        else:
            interval = self.parseInterval(request) if request.has('interval') else None

            sessions = self.storage.findSessionsInsideTimestamp(request.get('includeIncompleteEntries'), interval)

        sessions = [session.toDict() for session in sessions]
        sessions = {'sessions': sessions}
        return sessions


    def handlePipesRequest(self, request: RequestWrapper):

        if request.getAllParameters() == {'what'}:
            pipes = self.storage.findAllPipes()

        else:
            pipes = self.storage.findPipesForSessions(request.get('sessionsId'))

        pipes = [pipe.toDict() for pipe in pipes]
        pipes = {'pipes': pipes}
        return pipes


    def handleRecordsRequest(self, request: RequestWrapper):

        interval = self.parseInterval(request) if request.has('interval') else None

        records = self.storage.findRecordsForPipe(request.get('pipeId'), interval)

        records = [record.toDict() for record in records]
        records = {'records': records}
        return records


    @private
    def parseInterval(self, request):

        interval = request.get('interval')

        unit = Unit[interval.get('unit')]

        startPoint = TimePoint(interval.get('start'), unit)
        endPoint = TimePoint(interval.get('stop'), unit)

        interval = Interval(startPoint, endPoint)
        return interval
