# Internal
from src.common.decorators import *
from src.helper.request_wrapper import RequestWrapper
from src.data_source.storage.storage_factory import StorageFactory
from src.domain.request_handlers.i_request_handler import WrongRequest
from src.domain.request_handlers.read_request_handler import ReadRequestHandler
from src.domain.request_handlers.write_request_handler import WriteRequestHandler


@singleton
class EventRegistry:

    def __init__(self):

        databaseStorage = StorageFactory.getStorage()

        self.requestTypeHandlers = \
        {
            'get': ReadRequestHandler(databaseStorage),
            'set': WriteRequestHandler(databaseStorage)
        }


    @final
    def handleRequests(self, requests):
        return [self.handleRequest(request) for request in requests]


    def handleRequest(self, request: RequestWrapper):

        try:
            if request.getAllParameters() == {'type', 'data'}:

                requestType = request.get('type')
                requestData = request.get('data')

                if requestType in self.requestTypeHandlers:

                    handler = self.requestTypeHandlers.get(requestType)
                    return handler.handle(requestData)

                raise WrongRequest

        except WrongRequest:
            raise WrongRequest(str(request))
