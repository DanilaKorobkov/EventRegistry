from src.domain.request_handlers.support_request_checker import SupportedRequestChecker


# Supported request:
def test_1(RequestWithWrongType):

    assert not SupportedRequestChecker.isSupported(RequestWithWrongType)


def test_2(RequestWithWrongFields):

    assert not SupportedRequestChecker.isSupported(RequestWithWrongFields)


def test_3(GetAllSessionsRequest):

    assert SupportedRequestChecker.isSupported(GetAllSessionsRequest)


def test_4(GetSessionsInIntervalRequest):

    assert SupportedRequestChecker.isSupported(GetSessionsInIntervalRequest)


def test_5(GetAllPipesRequest):

    assert SupportedRequestChecker.isSupported(GetAllPipesRequest)


def test_6(GetPipesForSessionsRequest):

    assert SupportedRequestChecker.isSupported(GetPipesForSessionsRequest)


def test_7(GetPipeRecordsRequest):

    assert SupportedRequestChecker.isSupported(GetPipeRecordsRequest)


def test_8(GetPipeRecordsInIntervalRequest):

    assert SupportedRequestChecker.isSupported(GetPipeRecordsInIntervalRequest)


# Invalid requests:
def test_9(RequestWithoutWhat):

    assert not SupportedRequestChecker.isSupported(RequestWithoutWhat)


def test_10(RequestWithInvalidWhat):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidWhat)


def test_11(RequestWithInvalidIncludeIncompleteEntriesType):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidIncludeIncompleteEntriesType)


def test_12(RequestWithInvalidIntervalStartType):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidIntervalStartType)


def test_13(RequestWithInvalidIntervalStopType):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidIntervalStopType)


def test_14(RequestWithInvalidIntervalUnit):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidIntervalUnit)


def test_15(RequestWithInvalidField):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidField)


def test_16(RequestWithInvalidFieldInInterval):

    assert not SupportedRequestChecker.isSupported(RequestWithInvalidFieldInInterval)


def test_17(PipesForSessionsRequestWithInvalidField):

    assert not SupportedRequestChecker.isSupported(PipesForSessionsRequestWithInvalidField)


def test_18(PipesForSessionsRequestWithInvalidSessionsIdType):

    assert not SupportedRequestChecker.isSupported(PipesForSessionsRequestWithInvalidSessionsIdType)


def test_19(PipeRecordsRequestWithWrongField):

    assert not SupportedRequestChecker.isSupported(PipeRecordsRequestWithWrongField)


def test_20(PipeRecordsRequestWithWrongPipeIdType):

    assert not SupportedRequestChecker.isSupported(PipeRecordsRequestWithWrongPipeIdType)
