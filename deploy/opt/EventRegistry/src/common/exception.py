# Internal
from src.common.decorators import override
# Python


class EventRegistryException(Exception):

    def __str__(self):
        return str(self.toDict())


    def getDescription(self):
        return str()


    def toDict(self):

        dictionary = {}

        data = {'exception': self.__class__.__name__}

        if self.getDescription():
            data.update({'description': self.getDescription()})

        dictionary.update({'error': data})
        return dictionary


class InvalidRequest(EventRegistryException):

    def __init__(self, request):
        self.request = request


    @override
    def getDescription(self):
        return 'Received invalid request: {}'.format(str(self.request))
