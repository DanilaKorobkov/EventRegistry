from .i_request_handler import *


class ReadRequestHandler(IRequestHandler):

    def handle(self, request):

        if request['what'] == 'Pipes':

            return self.handlePipesRequest(request)

        if request['what'] == 'Sessions':

            return self.handleSessionsRequest(request)


    def handlePipesRequest(self, request):

        if request['sessionsId']:
            pipes = self.storage.findPipesForSessions(request['sessionsId'], request['includeRecords'])

        else:
            pipes = self.storage.findAllPipes(request['includeRecords'])

        pipes = [pipe.toDict() for pipe in pipes]
        pipes = {'pipes': pipes}
        return pipes


    def handleSessionsRequest(self, request):

        if request['timestamp'] and request['includeIncompleteEntries'] is not None:

            parameters = \
                {
                    'start': request['timestamp']['start'],
                    'stop': request['timestamp']['stop'],
                    'includeIncompleteEntries': request['includeIncompleteEntries']
                }

            sessions = self.storage.findSessionsInsideTimestamp(parameters)

        else:
            sessions = self.storage.findAllSessions()

        sessions = [session.toDict() for session in sessions]
        sessions = {'sessions': sessions}
        return sessions
