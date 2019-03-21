# Internal
from src.helper.time_point import Unit
from src.helper.request_wrapper import RequestWrapper


class RequestValidator:

    @classmethod
    def isValid(cls, request: RequestWrapper):

        if not request.getAllParameters() == {'type', 'data'}:
            return False

        if request.get('type') not in {'set', 'get'}:
            return False

        return cls.__isDataValid(request.get('data'))


    @classmethod
    def __isDataValid(cls, request: RequestWrapper):

        if request.get('what') not in {'Sessions', 'Pipes', 'Records'}:
            return  False

        if request.getAllParameters() == {'what'}:
            return True

        if request.get('what') == 'Sessions':

            if request.getAllParameters() != {'what', 'interval', 'includeIncompleteEntries'}:
                return False

            includeIncompleteEntriesType = type(request.get('includeIncompleteEntries'))

            isIntervalSupported = cls.__isIntervalValid(request.get('interval'))

            return True if isIntervalSupported and includeIncompleteEntriesType is bool else False

        if request.get('what') == 'Pipes':

            if request.getAllParameters() != {'what', 'sessionsId'}:
                return False

            sessionIdsType = type(request.get('sessionsId'))

            return True if sessionIdsType is list else False

        if request.get('what') == 'Records':

            if request.getAllParameters() == {'what', 'pipeId'}:

                pipeIdType = type(request.get('pipeId'))

                return True if pipeIdType is int else False

            if request.getAllParameters() == {'what', 'pipeId', 'interval'}:

                pipeIdType = type(request.get('pipeId'))

                isIntervalSupported = cls.__isIntervalValid(request.get('interval'))

                return True if isIntervalSupported and pipeIdType is int else False

        return False


    @staticmethod
    def __isIntervalValid(interval: RequestWrapper):

        if interval.getAllParameters() == {'start', 'stop', 'unit'}:

            startType = type(interval.get('start'))
            stopType = type(interval.get('stop'))

            try:
                unit = Unit[interval.get('unit')]

            except KeyError:
                unit = None

            return True if type(unit) is Unit and startType is int and stopType is int else False
