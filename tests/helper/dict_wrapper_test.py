from src.helper.dict_wrapper import DictWrapper
# Python
import pytest


@pytest.fixture(scope = 'module')
def WrappedDict():

    return DictWrapper({'key1': 0, 'key2': {'value': 0}})


@pytest.fixture(params = [{'key': 'key1','expectValue': 0}, {'key': 'key2','expectValue': DictWrapper({'value': 0})}, {'key': 'key3','expectValue': None}])
def Expectation(request):
    return request.param


def test_DictWrapper_hasAttribute_ifExists_returnTrueElseFalse(WrappedDict):

    assert WrappedDict.hasAttribute('key1') is True
    assert WrappedDict.hasAttribute('key3') is False


def test_DictWrapper_getItem_ifExists_returnItem(WrappedDict, Expectation):

    assert WrappedDict.getAttribute(Expectation['key']) == Expectation['expectValue']
