# Internal
from src.domain.objects.session import Session
from src.helper.interval import Unit, Interval
from src.mapper.mappers.session_mapper import SessionMapper
# Python
import pytest


@pytest.fixture(scope = 'module')
def Sessions():

    session1 = Session()
    session1.startUtcTime = '2019-03-13 06:23:36.386000'
    session1.stopUtcTime = '2019-03-13 06:23:41.736037'

    session2 = Session()
    session2.startUtcTime = '2019-03-13 07:21:12.601000'
    session2.stopUtcTime = '2019-03-13 07:21:18.538242'

    return [session1, session2]


def test_SessionMapper_findAll(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    sessions = mapper.findAll()

    assert sessions == Sessions


def test_SessionMapper_findInsideTimeStamp_InclusiveFalse(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    session1StartInSeconds = 1552447416.386
    session2StartInSeconds = 1552450872.601

    interval = Interval(session1StartInSeconds, session2StartInSeconds, Unit.Second)

    sessions = mapper.findInsideTimestamp(interval = interval, inclusive = False)

    assert sessions == [Sessions[0]]



def test_SessionMapper_findInsideTimeStamp_InclusiveTrue(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    session1StartInSeconds = 1552447416.386
    session2StartInSeconds = 1552450872.601

    interval = Interval(session1StartInSeconds, session2StartInSeconds, Unit.Second)

    sessions = mapper.findInsideTimestamp(interval = interval, inclusive = True)

    assert sessions == Sessions
