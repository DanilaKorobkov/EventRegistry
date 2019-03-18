from src.helper.time_point import TimePoint, Unit, WrongUnit
# Python
import pytest


def test_transformTo_Microsecond():

    timePoint = TimePoint(1, Unit.Millisecond)

    transformToMicrosecondTimePoint = timePoint.transformTo(Unit.Microsecond)

    assert transformToMicrosecondTimePoint.value == 1000
    assert transformToMicrosecondTimePoint.unit == Unit.Microsecond


def test_transformTo_Utc():

    timePoint = TimePoint(1552447416.386, Unit.Second)

    transformToMicrosecondTimePoint = timePoint.transformTo(Unit.Utc)

    assert transformToMicrosecondTimePoint.value == '2019-03-13 06:23:36.386000'
    assert transformToMicrosecondTimePoint.unit == Unit.Utc


def test_transformTo_SecondSinceEpoch():

    timePoint = TimePoint('2019-03-13 06:23:36.386000', Unit.Utc)

    transformToMicrosecondTimePoint = timePoint.transformTo(Unit.Millisecond)

    assert transformToMicrosecondTimePoint.value == 1552447416386
    assert transformToMicrosecondTimePoint.unit == Unit.Millisecond


def test_setAttribute_withUnknownUnit_raiseWrongUnit():

    timePoint = TimePoint(1, Unit.Millisecond)

    with pytest.raises(NotImplementedError):
        timePoint.value = 2

    with pytest.raises(NotImplementedError):
        timePoint.unit = 2

