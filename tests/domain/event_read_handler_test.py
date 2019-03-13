from src.domain.request_handlers.event_read_handler import EventReadHandler
# Internal
from src.helper.dict_wrapper import DictWrapper
# Python
import pytest


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
    return DictWrapper({'what': 'Sessions', 'timestamp': {'start': 1, 'stop': 2}, 'includeIncompleteEntries': True})


def test_EventReadHandler_handle(mocker, GetAllPipesRequest, GetAllSessionsRequest):

    eventReadHandler = EventReadHandler()

    mocker.patch.object(eventReadHandler, 'handlePipesRequest')
    mocker.patch.object(eventReadHandler, 'handleSessionsRequest')

    eventReadHandler.handle(GetAllPipesRequest)
    eventReadHandler.handle(GetAllSessionsRequest)

    eventReadHandler.handlePipesRequest.assert_called_once_with(GetAllPipesRequest)
    eventReadHandler.handleSessionsRequest.assert_called_once_with(GetAllSessionsRequest)


def test_EventReadHandler_handlePipesRequest_whenSessionsId_empty(mocker, GetAllPipesRequest):

    request = GetAllPipesRequest

    eventReadHandler = EventReadHandler()
    mocker.patch.object(eventReadHandler.storage, 'findAllPipes')

    eventReadHandler.handlePipesRequest(request)

    eventReadHandler.storage.findAllPipes.assert_called_once_with(request['includeRecords'])


def test_EventReadHandler_handlePipesRequest_whenSessionsId_notEmpty(mocker, GetPipesForSessionsRequestWithoutRecords):

    request = GetPipesForSessionsRequestWithoutRecords

    eventReadHandler = EventReadHandler()
    mocker.patch.object(eventReadHandler.storage, 'findPipesForSessions')

    eventReadHandler.handlePipesRequest(request)

    eventReadHandler.storage.findPipesForSessions.assert_called_once_with(request['sessionsId'], request['includeRecords'])


def test_EventReadHandler_handleSessionsRequest_whenTimestampOrIncludeIncompleteEntries_empty(mocker, GetAllSessionsRequest):

    eventReadHandler = EventReadHandler()
    mocker.patch.object(eventReadHandler.storage, 'findAllSessions')

    eventReadHandler.handleSessionsRequest(GetAllSessionsRequest)

    eventReadHandler.storage.findAllSessions.assert_called_once_with()


def test_EventReadHandler_handleSessionsRequest_whenTimestampAndIncludeIncompleteEntries_notEmpty(mocker, GetSessionsInsideTimestampRequest):

    request = GetSessionsInsideTimestampRequest

    eventReadHandler = EventReadHandler()
    mocker.patch.object(eventReadHandler.storage, 'findSessionsInsideTimestamp')

    eventReadHandler.handleSessionsRequest(request)

    parameters = \
        {
            'start': request['timestamp']['start'],
            'stop': request['timestamp']['stop'],
            'includeIncompleteEntries': request['includeIncompleteEntries']
        }
    eventReadHandler.storage.findSessionsInsideTimestamp.assert_called_once_with(parameters)
