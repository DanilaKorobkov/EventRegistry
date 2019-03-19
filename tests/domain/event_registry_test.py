# Internal
from src.common.exception import InvalidRequest
from src.domain.event_registry import EventRegistry
# Python
import pytest


def test_EventRegistry_handleRequest_GetRequest(mocker, GetAllSessionsRequest):

    eventRegistry = EventRegistry()
    readHandler = eventRegistry.requestTypeHandlers.get('get')
    mocker.patch.object(readHandler, 'handle')

    eventRegistry.handleRequest(GetAllSessionsRequest)

    readHandler.handle.assert_called_once_with(GetAllSessionsRequest.get('data'))


def test_EventRegistry_handleRequest_RequestWithWrongFields(RequestWithWrongFields):

    eventRegistry = EventRegistry()

    result =  eventRegistry.handleRequest(RequestWithWrongFields)

    assert result == {'error': {'exception': 'InvalidRequest',
                                'description': "Received invalid request: {'field1': 0, 'field2': 0}"}}


def test_EventRegistry_handleRequest_RequestWithWrongType(RequestWithWrongType):

    eventRegistry = EventRegistry()

    result = eventRegistry.handleRequest(RequestWithWrongType)

    assert result == {'error': {'exception': 'InvalidRequest',
                                'description': "Received invalid request: {'type': 'Wrong', 'data': {}}"}}