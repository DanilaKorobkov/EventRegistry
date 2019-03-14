# Internal
from src.domain.objects.session import Session
from src.mapper.mappers.session_mapper import SessionMapper
# Python
import pytest


@pytest.fixture(scope = 'module')
def Sessions():

    session1 = Session()
    session1.unit = 9.99999971718069e-10
    session1.startUtcTime = '2019-03-13 06:23:36.386286'
    session1.stopUtcTime = '2019-03-13 06:23:41.937364'

    session2 = Session()
    session2.unit = 9.99999971718069e-10
    session2.startUtcTime = '2019-03-13 07:21:12.601445'
    session2.stopUtcTime = '2019-03-13 07:21:18.539299'

    return [session1, session2]


def test_SessionMapper_findAll(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    sessions = mapper.findAll()

    assert sessions == Sessions


def test_SessionMapper_findInsideTimeStamp_InclusiveFalse(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    sessions = mapper.findInsideTimestamp(start = '2019-03-13 06:23:36.386286',
                                           stop = '2019-03-13 07:21:13.601445',
                                           inclusive = False)

    assert sessions == [Sessions[0]]



def test_SessionMapper_findInsideTimeStamp_InclusiveTrue(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    sessions = mapper.findInsideTimestamp(start = '2019-03-13 06:23:36.386286',
                                           stop = '2019-03-13 07:21:13.601445',
                                           inclusive = True)

    assert sessions == Sessions
