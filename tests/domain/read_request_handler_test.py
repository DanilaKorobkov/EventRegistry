from src.domain.request_handlers.read_request_handler import ReadRequestHandler
# Internal
from src.helper.interval import TimePoint, Unit, Interval
from src.helper.request_wrapper import RequestWrapper
# Python
import pytest
from unittest.mock import MagicMock


@pytest.fixture(scope = 'module')
def SecondInterval():

    return Interval(TimePoint(1, Unit.Second),
                    TimePoint(2, Unit.Second))


@pytest.fixture(scope = 'module')
def GetAllSessionsRequest():
    return RequestWrapper({'what': 'Sessions'})


@pytest.fixture(scope = 'module')
def GetSessionsInIntervalRequest():
    return RequestWrapper({'what': 'Sessions',
                           'includeIncompleteEntries': False,
                           'interval': {'start': 1, 'stop': 2, 'unit': 'Second'}})


@pytest.fixture(scope = 'module')
def GetAllPipesRequest():
    return RequestWrapper({'what': 'Pipes'})


@pytest.fixture(scope = 'module')
def GetPipesForSessionsRequest():
    return RequestWrapper({'what': 'Pipes',
                           'sessionsId': [1, 2]})


@pytest.fixture(scope = 'module')
def GetPipeRecordsRequest():
    return RequestWrapper({'what': 'Records',
                           'pipeId': 1})


@pytest.fixture(scope = 'module')
def GetPipeRecordsInIntervalRequest():
    return RequestWrapper({'what': 'Records',
                           'pipeId': 1,
                           'interval': {'start': 1, 'stop': 2, 'unit': 'Second'}})


@pytest.fixture
def StorageMock():

    storage = MagicMock()

    storage.findAllSessions = MagicMock()
    storage.findRecordsForPipe = MagicMock()
    storage.findPipesForSessions = MagicMock()
    storage.findSessionsInsideTimestamp = MagicMock()

    return storage


def test_ReadRequestHandler_handle(StorageMock, GetAllPipesRequest, GetAllSessionsRequest, GetPipeRecordsRequest):

    eventReadHandler = ReadRequestHandler(StorageMock)
    eventReadHandler.handlePipesRequest = MagicMock()
    eventReadHandler.handleSessionsRequest = MagicMock()
    eventReadHandler.handleRecordsRequest = MagicMock()

    eventReadHandler.handle(GetAllPipesRequest)
    eventReadHandler.handle(GetAllSessionsRequest)
    eventReadHandler.handle(GetPipeRecordsRequest)

    eventReadHandler.handlePipesRequest.assert_called_once_with(GetAllPipesRequest)
    eventReadHandler.handleSessionsRequest.assert_called_once_with(GetAllSessionsRequest)
    eventReadHandler.handleRecordsRequest.assert_called_once_with(GetPipeRecordsRequest)


def test_ReadRequestHandler_handleSessionsRequest_All(GetAllSessionsRequest, StorageMock):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleSessionsRequest(GetAllSessionsRequest)

    StorageMock.findAllSessions.assert_called_once()


def test_ReadRequestHandler_handleSessionsRequest_InInterval(GetSessionsInIntervalRequest, SecondInterval, StorageMock):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleSessionsRequest(GetSessionsInIntervalRequest)

    StorageMock.findSessionsInsideTimestamp.assert_called_once_with(False, SecondInterval)



def test_ReadRequestHandler_handlePipesRequest_All(StorageMock, GetAllPipesRequest):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest(GetAllPipesRequest)

    StorageMock.findAllPipes.assert_called_once()


def test_ReadRequestHandler_handlePipesRequest_PipesForSessions(StorageMock, GetPipesForSessionsRequest):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest(GetPipesForSessionsRequest)

    StorageMock.findPipesForSessions.assert_called_once_with([1, 2])



def test_handleRecordsRequest(GetPipeRecordsInIntervalRequest, GetPipeRecordsRequest, StorageMock, SecondInterval):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleRecordsRequest(GetPipeRecordsRequest)
    StorageMock.findRecordsForPipe.assert_called_with(1, None)

    eventReadHandler.handleRecordsRequest(GetPipeRecordsInIntervalRequest)
    StorageMock.findRecordsForPipe.assert_called_with(1, SecondInterval)

