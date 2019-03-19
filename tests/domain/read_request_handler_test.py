from src.domain.request_handlers.read_request_handler import ReadRequestHandler
# Internal
from src.helper.interval import TimePoint, Unit, Interval
from src.helper.request_wrapper import RequestWrapper
# Python
import pytest
from unittest.mock import MagicMock


def test_ReadRequestHandler_handle(StorageMock,
                                   _GetAllPipesRequestData,
                                   _GetAllSessionsRequestData,
                                   _GetPipeRecordsRequestData):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest = MagicMock()
    eventReadHandler.handleSessionsRequest = MagicMock()
    eventReadHandler.handleRecordsRequest = MagicMock()

    eventReadHandler.handle(_GetAllPipesRequestData)
    eventReadHandler.handle(_GetAllSessionsRequestData)
    eventReadHandler.handle(_GetPipeRecordsRequestData)

    eventReadHandler.handlePipesRequest.assert_called_once_with(_GetAllPipesRequestData)
    eventReadHandler.handleSessionsRequest.assert_called_once_with(_GetAllSessionsRequestData)
    eventReadHandler.handleRecordsRequest.assert_called_once_with(_GetPipeRecordsRequestData)


def test_ReadRequestHandler_handleSessionsRequest_All(_GetAllSessionsRequestData, StorageMock):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleSessionsRequest(_GetAllSessionsRequestData)

    StorageMock.findAllSessions.assert_called_once()


def test_ReadRequestHandler_handleSessionsRequest_InInterval(_GetSessionsInIntervalRequestData,
                                                             SecondInterval,
                                                             StorageMock):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleSessionsRequest(_GetSessionsInIntervalRequestData)

    StorageMock.findSessionsInsideTimestamp.assert_called_once_with(False, SecondInterval)



def test_ReadRequestHandler_handlePipesRequest_All(StorageMock, _GetAllPipesRequestData):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest(_GetAllPipesRequestData)

    StorageMock.findAllPipes.assert_called_once()


def test_ReadRequestHandler_handlePipesRequest_PipesForSessions(StorageMock, _GetPipesForSessionsRequestData):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handlePipesRequest(_GetPipesForSessionsRequestData)

    StorageMock.findPipesForSessions.assert_called_once_with([1, 2])



def test_handleRecordsRequest(_GetPipeRecordsRequestData,
                              _GetPipeRecordsInIntervalRequestData,
                              StorageMock,
                              SecondInterval):

    eventReadHandler = ReadRequestHandler(StorageMock)

    eventReadHandler.handleRecordsRequest(_GetPipeRecordsRequestData)
    StorageMock.findRecordsForPipe.assert_called_with(1, None)

    eventReadHandler.handleRecordsRequest(_GetPipeRecordsInIntervalRequestData)
    StorageMock.findRecordsForPipe.assert_called_with(1, SecondInterval)

