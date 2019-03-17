# Internal
from src.domain.event_registry import EventRegistry, WrongRequest
# Python
import pytest


def test_eventRegistry_handleRequest(mocker, GetRequest, SetRequest, RequestWithWrongType, RequestWithWrongFields):

    eventRegistry = EventRegistry()

    readHandler = eventRegistry.requestTypeHandlers.get('get')
    writeHandler = eventRegistry.requestTypeHandlers.get('set')

    mocker.patch.object(readHandler, 'handle')
    mocker.patch.object(writeHandler, 'handle')

    eventRegistry.handleRequest(GetRequest)
    eventRegistry.handleRequest(SetRequest)

    with pytest.raises(WrongRequest):
        eventRegistry.handleRequest(RequestWithWrongType)

    with pytest.raises(WrongRequest):
        eventRegistry.handleRequest(RequestWithWrongFields)

    readHandler.handle.assert_called_once_with(GetRequest.get('data'))
    writeHandler.handle.assert_called_once_with(SetRequest.get('data'))

