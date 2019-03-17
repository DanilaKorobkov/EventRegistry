from .i_request_handler import *
# Internal
from src.helper.interval import Unit, Interval
from src.helper.dict_wrapper import DictWrapper
from src.domain.converters.date_time_converter import DateTimeConverter


class ReadRequestHandler(IRequestHandler):

    def handle(self, request: DictWrapper):

        if request.get('what') == 'Pipes':

            return self.handlePipesRequest(request)

        if request.get('what') == 'Sessions':

            return self.handleSessionsRequest(request)


    def handlePipesRequest(self, request: DictWrapper):

        if request.has('sessionsId'):

            interval = None

            if request.has('interval'):

                interval = request.get('interval')

                start = interval.getAttribute('start')
                stop = interval.getAttribute('stop')
                unit = Unit[interval.getAttribute('unit')]

                interval = Interval(start, stop, unit)

            pipes = self.storage.findPipesForSessions(request.get('sessionsId'), request.get('includeRecords'), interval)

        else:
            pipes = self.storage.findAllPipes(request.get('includeRecords'))

        pipes = [pipe.toDict() for pipe in pipes]
        pipes = {'pipes': pipes}
        return pipes


    def handleSessionsRequest(self, request: DictWrapper):

        if request.has('interval') and request.has('includeIncompleteEntries'):

            start = self.fromMicroSecToSec(request.get('interval').get('start'))
            stop = self.fromMicroSecToSec(request.get('interval').get('stop'))

            parameters = \
                {
                    'start': DateTimeConverter.translateSecondsSinceEpochToUtc(start),
                    'stop': DateTimeConverter.translateSecondsSinceEpochToUtc(stop),
                    'includeIncompleteEntries': request.get('includeIncompleteEntries')
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
