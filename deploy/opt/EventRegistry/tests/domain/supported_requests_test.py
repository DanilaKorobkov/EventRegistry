from src.domain.request_handlers.request_validator import RequestValidator


# Supported request:
def test_1(RequestWithWrongType):

    assert not RequestValidator.isValid(RequestWithWrongType)


def test_2(RequestWithWrongFields):

    assert not RequestValidator.isValid(RequestWithWrongFields)


def test_3(GetAllSessionsRequest):

    assert RequestValidator.isValid(GetAllSessionsRequest)


def test_4(GetSessionsInIntervalRequest):

    assert RequestValidator.isValid(GetSessionsInIntervalRequest)


def test_5(GetAllPipesRequest):

    assert RequestValidator.isValid(GetAllPipesRequest)


def test_6(GetPipesForSessionsRequest):

    assert RequestValidator.isValid(GetPipesForSessionsRequest)


def test_7(GetPipeRecordsRequest):

    assert RequestValidator.isValid(GetPipeRecordsRequest)


def test_8(GetPipeRecordsInIntervalRequest):

    assert RequestValidator.isValid(GetPipeRecordsInIntervalRequest)


# Invalid requests:
def test_9(RequestWithoutWhat):

    assert not RequestValidator.isValid(RequestWithoutWhat)


def test_10(RequestWithInvalidWhat):

    assert not RequestValidator.isValid(RequestWithInvalidWhat)


def test_11(RequestWithInvalidIncludeIncompleteEntriesType):

    assert not RequestValidator.isValid(RequestWithInvalidIncludeIncompleteEntriesType)


def test_12(RequestWithInvalidIntervalStartType):

    assert not RequestValidator.isValid(RequestWithInvalidIntervalStartType)


def test_13(RequestWithInvalidIntervalStopType):

    assert not RequestValidator.isValid(RequestWithInvalidIntervalStopType)


def test_14(RequestWithInvalidIntervalUnit):

    assert not RequestValidator.isValid(RequestWithInvalidIntervalUnit)


def test_15(RequestWithInvalidField):

    assert not RequestValidator.isValid(RequestWithInvalidField)


def test_16(RequestWithInvalidFieldInInterval):

    assert not RequestValidator.isValid(RequestWithInvalidFieldInInterval)


def test_17(PipesForSessionsRequestWithInvalidField):

    assert not RequestValidator.isValid(PipesForSessionsRequestWithInvalidField)


def test_18(PipesForSessionsRequestWithInvalidSessionsIdType):

    assert not RequestValidator.isValid(PipesForSessionsRequestWithInvalidSessionsIdType)


def test_19(PipeRecordsRequestWithWrongField):

    assert not RequestValidator.isValid(PipeRecordsRequestWithWrongField)


def test_20(PipeRecordsRequestWithWrongPipeIdType):

    assert not RequestValidator.isValid(PipeRecordsRequestWithWrongPipeIdType)
