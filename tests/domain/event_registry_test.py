# Internal
from src.domain.event_registry import EventRegistry, WrongRequestType
# Python
import pytest


def test_eventRegistry_handleRequest(mocker, GetRequest, SetRequest, RequestWithWrongType):

    eventRegistry = EventRegistry()

    mocker.patch.object(eventRegistry.readRequestHandler, 'handle')
    mocker.patch.object(eventRegistry.writeRequestHandler, 'handle')

    eventRegistry.handleRequest(GetRequest)
    eventRegistry.handleRequest(SetRequest)

    with pytest.raises(WrongRequestType):
        eventRegistry.handleRequest(RequestWithWrongType)

    eventRegistry.readRequestHandler.handle.assert_called_once_with(GetRequest['data'])
    eventRegistry.writeRequestHandler.handle.assert_called_once_with(SetRequest['data'])

