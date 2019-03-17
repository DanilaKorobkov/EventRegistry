# Python
from enum import unique, Enum


@unique
class Unit(Enum):

    Second = 0
    Millisecond = -3
    Microsecond = -6
    Nanoseconds = -9


class WrongUnit(Exception):
    pass


class Interval:

    def __init__(self, start, stop, unit: Unit):

        if type(unit) is not Unit:
            raise WrongUnit

        self.start = start
        self.stop = stop

        self.currentUnit = unit


    def transformTo(self, unit: Unit):

        if type(unit) is not Unit:
            raise WrongUnit

        coefficient = 1 * 10 ** (self.currentUnit.value - unit.value)

        interval = Interval(self.start * coefficient, self.stop * coefficient, unit)
        return interval


    def __eq__(self, other):

        return all((self.currentUnit == other.currentUnit,
                    self.start == other.start,
                    self.stop == other.stop))


    def __setattr__(self, key, value):

        if key in {'start', 'stop', 'currentUnit'}:

            try:
                getattr(self, key)

            except AttributeError:
                object.__setattr__(self, key, value)
                return

        raise NotImplementedError
