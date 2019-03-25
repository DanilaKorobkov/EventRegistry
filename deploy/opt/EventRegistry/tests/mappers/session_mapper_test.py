# Internal
from src.domain.objects.session import Session
from src.helper.interval import Interval
from src.helper.time_point import TimePoint, Unit
from src.mapper.mappers.session_mapper import SessionMapper
# Python
import pytest


@pytest.fixture(scope = 'module')
def Sessions():

    session1 = Session()
    session1.interval = Interval(TimePoint('2019-03-13 06:23:36.386000', Unit.Utc).transformTo(Unit.Second),
                                 TimePoint('2019-03-13 06:23:41.736037', Unit.Utc).transformTo(Unit.Second))

    session2 = Session()
    session2.interval = Interval(TimePoint('2019-03-13 07:21:12.601000', Unit.Utc).transformTo(Unit.Second),
                                 TimePoint('2019-03-13 07:21:18.538242', Unit.Utc).transformTo(Unit.Second))

    return [session1, session2]


def test_SessionMapper_findAll(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    sessions = mapper.findAll()

    assert sessions == Sessions


def test_SessionMapper_findInsideTimeStamp_InclusiveFalse(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    interval = Interval(TimePoint(1552447416.386, Unit.Second),
                        TimePoint(1552450872.601, Unit.Second))

    sessions = mapper.findInsideTimestamp(includeIncompleteEntries = False, interval = interval)

    assert sessions == [Sessions[0]]



def test_SessionMapper_findInsideTimeStamp_InclusiveTrue(DatabaseConnection, Sessions):

    mapper = SessionMapper(DatabaseConnection)

    interval = Interval(TimePoint(1552447416.386, Unit.Second),
                        TimePoint(1552450872.601, Unit.Second))

    sessions = mapper.findInsideTimestamp(includeIncompleteEntries = True, interval = interval)

    assert sessions == Sessions
