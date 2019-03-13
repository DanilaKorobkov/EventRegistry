# Internal
from src.common.decorators import singleton
from src.helper.dict_wrapper import DictWrapper
from src.domain.request_handlers.event_read_handler import EventReadHandler
from src.domain.request_handlers.event_write_handler import EventWriteHandler


class WrongRequestType(Exception):
    pass


@singleton
class EventRegistry:

    def __init__(self):

        self.eventReadHandler = EventReadHandler()
        self.eventWriteHandler = EventWriteHandler()


    def handleRequests(self, requests):

        return [self.handleRequest(request) for request in requests]


    def handleRequest(self, request: DictWrapper):

        if request['type'] == 'get':
            return self.eventReadHandler.handle(request['data'])

        elif request['type'] == 'set':
            return self.eventWriteHandler.handle(request['data'])

        raise WrongRequestType(str(request))
