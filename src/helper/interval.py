# Internal
from .time_point import TimePoint, Unit, WrongUnit



class Interval:

    def __init__(self, start: TimePoint, stop: TimePoint):

        self.start = start
        self.stop = stop.transformTo(start.unit)


    def transformTo(self, unit: Unit):

        if type(unit) is not Unit:
            raise WrongUnit

        interval = Interval(self.start.transformTo(unit), self.stop.transformTo(unit))
        return interval


    def __eq__(self, other):

        return all((self.start == other.start,
                    self.stop == other.stop))


    def __setattr__(self, key, value):

        if key in {'start', 'stop'}:

            try:
                getattr(self, key)

            except AttributeError:
                object.__setattr__(self, key, value)
                return

        raise NotImplementedError
