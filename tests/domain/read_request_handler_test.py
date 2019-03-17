from src.domain.request_handlers.read_request_handler import ReadRequestHandler
# Internal
from src.helper.dict_wrapper import DictWrapper
from src.domain.converters.date_time_converter import DateTimeConverter
# Python
import pytest
from unittest.mock import MagicMock


@pytest.fixture(scope = 'module')
def GetAllPipesRequest():
    return DictWrapper({'what': 'Pipes', 'includeRecords': False})


@pytest.fixture(scope = 'module')
def GetPipesForSessionsRequestWithoutRecords():
    return DictWrapper({'what': 'Pipes', 'sessionsId': [1, 2], 'includeRecords': False})


@pytest.fixture(scope = 'module')
def GetAllSessionsRequest():
    return DictWrapper({'what': 'Sessions'})


@pytest.fixture(scope = 'module')
def GetSessionsInsideTimestampRequest():
    return DictWrapper({'what': 'Sessions', 'interval': {'start': 1, 'stop': 2}, 'includeIncompleteEntries': True})


@pytest.fixture
def StorageMock():

    storage = MagicMock()

    storage.findAllSessions = MagicMock()
    storage.findPipesForSessions = MagicMock()
    storage.findSessionsInsideTimestamp = MagicMock()

    return storage


def test_ReadRequestHandler_handle(StorageMock, GetAllPipesRequest, GetAllSessionsRequest):

    eventReadHandler = ReadRequestHandler(StorageMock)
    eventReadHandler.handlePipesRequest = MagicMock()
    eventReadHandler.handleSessionsRequest = MagicMock()

    eventReadHandler.handle(GetAllPipesRequest)
    eventReadHandler.handle(GetAllSessionsRequest)

    eventReadHandler.handlePipesRequest.assert_called_once_with(GetAllPipesRequest)
    eventReadHandler.handleSessionsRequest.assert_called_once_with(GetAllSessionsRequest)


def test_ReadRequestHandler_handlePipesRequest_whenSessionsId_empty(StorageMock, GetAllPipesRequest):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest(GetAllPipesRequest)

    StorageMock.findAllPipes.assert_called_once_with(GetAllPipesRequest.get('includeRecords'))


def test_ReadRequestHandler_handlePipesRequest_whenSessionsId_notEmpty(StorageMock, GetPipesForSessionsRequestWithoutRecords):

    request = GetPipesForSessionsRequestWithoutRecords

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest(request)

    StorageMock.findPipesForSessions.assert_called_once_with(request.get('sessionsId'),
                                                             request.get('includeRecords'),
                                                             None)


def test_ReadRequestHandler_handleSessionsRequest_whenTimestampOrIncludeIncompleteEntries_empty(StorageMock, GetAllSessionsRequest):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleSessionsRequest(GetAllSessionsRequest)

    StorageMock.findAllSessions.assert_called_once_with()


def test_ReadRequestHandler_handleSessionsRequest_whenTimestampAndIncludeIncompleteEntries_notEmpty(StorageMock, GetSessionsInsideTimestampRequest):

    request = GetSessionsInsideTimestampRequest

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleSessionsRequest(request)

    parameters = \
        {
            'start': DateTimeConverter.translateSecondsSinceEpochToUtc(request.get('interval').get('start') / 1e6),
            'stop': DateTimeConverter.translateSecondsSinceEpochToUtc(request.get('interval').get('stop') / 1e6),
            'includeIncompleteEntries': request.get('includeIncompleteEntries')
        }
    StorageMock.findSessionsInsideTimestamp.assert_called_once_with(parameters)
