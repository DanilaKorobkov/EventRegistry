from .i_request_handler import *
# Internal
from src.domain.converters.date_time_converter import DateTimeConverter


class ReadRequestHandler(IRequestHandler):

    def handle(self, request):

        if request['what'] == 'Pipes':

            return self.handlePipesRequest(request)

        if request['what'] == 'Sessions':

            return self.handleSessionsRequest(request)


    def handlePipesRequest(self, request):

        if request['interval']:

            start = self.fromMicroSecToSec(request['interval']['start'])
            stop = self.fromMicroSecToSec(request['interval']['stop'])

            start = DateTimeConverter.translateSecondsSinceEpochToUtc(start)
            stop = DateTimeConverter.translateSecondsSinceEpochToUtc(stop)

        if request['sessionsId']:
            pipes = self.storage.findPipesForSessions(request['sessionsId'], request['includeRecords'])

        else:
            pipes = self.storage.findAllPipes(request['includeRecords'])

        pipes = [pipe.toDict() for pipe in pipes]
        pipes = {'pipes': pipes}
        return pipes


    def handleSessionsRequest(self, request):

        if request['interval'] and request['includeIncompleteEntries'] is not None:

            start = self.fromMicroSecToSec(request['interval']['start'])
            stop = self.fromMicroSecToSec(request['interval']['stop'])

            parameters = \
                {
                    'start': DateTimeConverter.translateSecondsSinceEpochToUtc(start),
                    'stop': DateTimeConverter.translateSecondsSinceEpochToUtc(stop),
                    'includeIncompleteEntries': request['includeIncompleteEntries']
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
