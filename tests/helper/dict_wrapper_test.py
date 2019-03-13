# Internal
from src.helper.dict_wrapper import DictWrapper
# Python
import pytest


@pytest.fixture(scope = 'session')
def WrappedDict():

    return DictWrapper({'key1': 0, 'key2': {'value': 0}})


@pytest.fixture(params = [{'key': 'key1','expectValue': 0}, {'key': 'key2','expectValue': DictWrapper({'value': 0})}, {'key': 'key3','expectValue': None}])
def Expectation(request):
    return request.param


def test_JsonWrapper_getItem_ifExists_returnItem(WrappedDict, Expectation):

    assert WrappedDict[Expectation['key']] == Expectation['expectValue']



def test_JsonWrapper_setItem(WrappedDict):

    WrappedDict['key2'] = 2

    assert WrappedDict['key2'] == 2

