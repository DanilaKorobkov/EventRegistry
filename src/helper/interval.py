# Python
from enum import unique, Enum


@unique
class Unit(Enum):

    Second = 0
    Millisecond = -3
    Microsecond = -6
    Nanoseconds = -9

    Unknown = None

class WrongUnit(Exception):
    pass


class Interval:

    def __init__(self, start, stop, unit: Unit):

        if unit == Unit.Unknown:
            raise WrongUnit

        self.start = start
        self.stop = stop

        self.currentUnit = unit


    def __eq__(self, other):

        return all((self.currentUnit == other.currentUnit,
                    self.start == other.start,
                    self.stop == other.stop))


    def setValue(self, start, stop, unit: Unit):

        if unit == Unit.Unknown:
            raise WrongUnit

        self.start = start
        self.stop = stop

        self.currentUnit = unit


    def transformTo(self, unit: Unit):

        if unit == Unit.Unknown:
            raise WrongUnit

        coefficient = 1 * 10 ** (self.currentUnit.value - unit.value)

        interval = Interval(self.start, self.stop, self.currentUnit)
        interval.start = self.start * coefficient
        interval.stop = self.stop * coefficient
        interval.currentUnit = unit

        return interval
