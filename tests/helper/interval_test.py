from src.helper.interval import Interval, Unit, WrongUnit
# Python
import pytest


def test_init_withUnknownUnit_raiseWrongUnit():

    with pytest.raises(WrongUnit):
        Interval(1, 2, Unit.Unknown)


def test_setValue_withUnknownUnit_raiseWrongUnit():

    interval = Interval(1, 2, Unit.Second)

    with pytest.raises(WrongUnit):
        interval.setValue(2, 3, Unit.Unknown)


def test_transformTo_withUnknownUnit_raiseWrongUnit():

    interval = Interval(1, 2, Unit.Second)

    with pytest.raises(WrongUnit):
        interval.transformTo(Unit.Unknown)


def test_transformTo_Seconds():

    millisecondsInterval = Interval(1, 2, Unit.Millisecond)

    transformToMicrosecondInterval = millisecondsInterval.transformTo(Unit.Microsecond)

    assert millisecondsInterval.start == 1
    assert millisecondsInterval.stop == 2
    assert millisecondsInterval.currentUnit == Unit.Millisecond

    assert transformToMicrosecondInterval.start == 1000
    assert transformToMicrosecondInterval.stop == 2000
    assert transformToMicrosecondInterval.currentUnit == Unit.Microsecond

