# Python
import time
from copy import deepcopy
from datetime import datetime
from enum import unique, Enum


@unique
class Unit(Enum):

    Second = 0
    Millisecond = -3
    Microsecond = -6
    Nanoseconds = -9

    Utc = 25


class WrongUnit(Exception):
    pass


class TimePoint:

    def __init__(self, value, unit: Unit):

        if type(unit) is not Unit:
            raise WrongUnit

        self.value = value
        self.unit = unit


    def transformTo(self, unit: Unit):

        if type(unit) is not Unit:
            raise WrongUnit

        if self.unit == unit:
            return deepcopy(self)

        if self.unit == Unit.Utc:

            dotIndex = self.value.rfind('.')
            dataTime = self.value[: dotIndex + 6 + 1]

            dataTime = datetime.strptime(dataTime, '%Y-%m-%d %H:%M:%S.%f')
            secondsSinceEpoch = time.mktime(dataTime.timetuple()) + dataTime.microsecond / 1e6

            return TimePoint(secondsSinceEpoch, Unit.Second).transformTo(unit)


        if unit == Unit.Utc:

            utcTime = datetime.fromtimestamp(self.transformTo(Unit.Second).value).strftime('%Y-%m-%d %H:%M:%S.%f')

            timePoint = TimePoint(utcTime, Unit.Utc)
            return timePoint


        coefficient = 1 * 10 ** (self.unit.value - unit.value)

        timePoint = TimePoint(self.value * coefficient, unit)
        return timePoint


    def __eq__(self, other):

        return all((self.unit == other.unit,
                    self.value == other.value))


    def __setattr__(self, key, value):

        if key in {'value', 'unit'}:

            try:
                getattr(self, key)

            except AttributeError:
                object.__setattr__(self, key, value)
                return

        raise NotImplementedError
