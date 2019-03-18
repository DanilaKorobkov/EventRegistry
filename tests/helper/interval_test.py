from src.helper.interval import Interval
# Internal
from src.helper.time_point import TimePoint, Unit, WrongUnit
# Python
import pytest
from copy import deepcopy


@pytest.fixture
def MillisecondInterval():

    startPoint = TimePoint(1, Unit.Millisecond)
    endPoint = TimePoint(2, Unit.Millisecond)

    interval = Interval(startPoint, endPoint)
    return interval


def test_transformTo_Seconds(MillisecondInterval):

    tmp = deepcopy(MillisecondInterval)

    transformToMicrosecondInterval = MillisecondInterval.transformTo(Unit.Microsecond)

    assert tmp.start == MillisecondInterval.start
    assert tmp.stop == MillisecondInterval.stop

    assert transformToMicrosecondInterval.start == TimePoint(1000, Unit.Microsecond)
    assert transformToMicrosecondInterval.stop == TimePoint(2000, Unit.Microsecond)


def test_setAttribute_withUnknownUnit_raiseWrongUnit(MillisecondInterval):

    with pytest.raises(NotImplementedError):
        MillisecondInterval.start = 2

    with pytest.raises(NotImplementedError):
        MillisecondInterval.stop = 2
