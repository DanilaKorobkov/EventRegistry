from .i_request_handler import *
# Internal
from src.helper.dict_wrapper import DictWrapper
from src.domain.converters.date_time_converter import DateTimeConverter


class ReadRequestHandler(IRequestHandler):

    def handle(self, request: DictWrapper):

        if request.getAttribute('what') == 'Pipes':

            return self.handlePipesRequest(request)

        if request.getAttribute('what') == 'Sessions':

            return self.handleSessionsRequest(request)


    def handlePipesRequest(self, request: DictWrapper):

        if request.hasAttribute('interval'):

            start = self.fromMicroSecToSec(request.getAttribute('interval').getAttribute('start'))
            stop = self.fromMicroSecToSec(request.getAttribute('interval').getAttribute('stop'))

            start = DateTimeConverter.translateSecondsSinceEpochToUtc(start)
            stop = DateTimeConverter.translateSecondsSinceEpochToUtc(stop)

        if request.hasAttribute('sessionsId'):
            pipes = self.storage.findPipesForSessions(request.getAttribute('sessionsId'), request.getAttribute('includeRecords'))

        else:
            pipes = self.storage.findAllPipes(request.getAttribute('includeRecords'))

        pipes = [pipe.toDict() for pipe in pipes]
        pipes = {'pipes': pipes}
        return pipes


    def handleSessionsRequest(self, request: DictWrapper):

        if request.hasAttribute('interval') and request.hasAttribute('includeIncompleteEntries'):

            start = self.fromMicroSecToSec(request.getAttribute('interval').getAttribute('start'))
            stop = self.fromMicroSecToSec(request.getAttribute('interval').getAttribute('stop'))

            parameters = \
                {
                    'start': DateTimeConverter.translateSecondsSinceEpochToUtc(start),
                    'stop': DateTimeConverter.translateSecondsSinceEpochToUtc(stop),
                    'includeIncompleteEntries': request.getAttribute('includeIncompleteEntries')
                }

            sessions = self.storage.findSessionsInsideTimestamp(parameters)

        else:
            sessions = self.storage.findAllSessions()

        sessions = [session.toDict() for session in sessions]
        sessions = {'sessions': sessions}
        return sessions


    @staticmethod
    def fromMicroSecToSec(microseconds):
        return microseconds / 1e6
