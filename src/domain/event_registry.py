# Internal
from src.common.decorators import *
from src.helper.request_wrapper import RequestWrapper
from src.data_source.storage.storage_factory import StorageFactory
from src.common.exception import InvalidRequest, EventRegistryException
from .request_handlers.support_request_checker import SupportedRequestChecker
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

        if not SupportedRequestChecker.isSupported(request):
            raise InvalidRequest(request)

        requestType = request.get('type')
        requestData = request.get('data')

        if requestType in self.requestTypeHandlers:

            handler = self.requestTypeHandlers.get(requestType)
            return handler.handle(requestData)
