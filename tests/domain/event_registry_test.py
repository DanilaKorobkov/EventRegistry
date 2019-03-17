# Internal
from src.domain.event_registry import EventRegistry, WrongRequest
# Python
import pytest


def test_EventRegistry_handleRequest_GetRequest(mocker, GetRequest):

    eventRegistry = EventRegistry()
    readHandler = eventRegistry.requestTypeHandlers.get('get')
    mocker.patch.object(readHandler, 'handle')

    eventRegistry.handleRequest(GetRequest)

    readHandler.handle.assert_called_once_with(GetRequest.get('data'))


def test_EventRegistry_handleRequest_SetRequest(mocker, SetRequest):

    eventRegistry = EventRegistry()
    writeHandler = eventRegistry.requestTypeHandlers.get('set')
    mocker.patch.object(writeHandler, 'handle')

    eventRegistry.handleRequest(SetRequest)

    writeHandler.handle.assert_called_once_with(SetRequest.get('data'))


def test_EventRegistry_handleRequest_RequestWithWrongFields(RequestWithWrongFields):

    eventRegistry = EventRegistry()

    with pytest.raises(WrongRequest):
        eventRegistry.handleRequest(RequestWithWrongFields)


def test_EventRegistry_handleRequest_RequestWithWrongType(RequestWithWrongType):

    eventRegistry = EventRegistry()

    with pytest.raises(WrongRequest):
        eventRegistry.handleRequest(RequestWithWrongType)
