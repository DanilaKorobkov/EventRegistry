# Internal
from src.common.decorators import singleton
from src.helper.dict_wrapper import DictWrapper
from src.data_source.storage_factory import StorageFactory
from src.domain.request_handlers.read_request_handler import ReadRequestHandler
from src.domain.request_handlers.write_request_handler import WriteRequestHandler


class WrongRequestType(Exception):
    pass


@singleton
class EventRegistry:

    def __init__(self):

        databaseStorage = StorageFactory.getDatabaseStorage()

        self.readRequestHandler = ReadRequestHandler(databaseStorage)
        self.writeRequestHandler = WriteRequestHandler(databaseStorage)


    def handleRequests(self, requests):

        return [self.handleRequest(request) for request in requests]


    def handleRequest(self, request: DictWrapper):

        if request.get('type') == 'get':
            return self.readRequestHandler.handle(request.get('data'))

        elif request.get('type') == 'set':
            return self.writeRequestHandler.handle(request.get('data'))

        raise WrongRequestType(str(request))
