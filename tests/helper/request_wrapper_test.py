from src.helper.request_wrapper import RequestWrapper
# Python
import pytest


@pytest.fixture(scope = 'module')
def WrapRequest():

    return RequestWrapper({'key1': 0, 'key2': {'value': 0}})


@pytest.fixture(params = [{'key': 'key1','expectValue': 0},
                          {'key': 'key2','expectValue': RequestWrapper({'value': 0})},
                          {'key': 'key3','expectValue': None}])
def Expectation(request):
    return request.param


def test_RequestWrapper_hasAttribute_ifExists_returnTrueElseFalse(WrapRequest):

    assert WrapRequest.has('key1') is True
    assert WrapRequest.has('key3') is False


def test_RequestWrapper_getItem_ifExists_returnItem(WrapRequest, Expectation):

    assert WrapRequest.get(Expectation['key']) == Expectation['expectValue']


def test_RequestWrapper_getAllParameters(WrapRequest):

    assert WrapRequest.getAllParameters() == {'key1', 'key2'}
    assert WrapRequest.get('key2').getAllParameters() == {'value'}