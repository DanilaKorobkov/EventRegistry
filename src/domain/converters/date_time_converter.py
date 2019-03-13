# Python
import time
from datetime import datetime


class DateTimeConverter:

    @classmethod
    def translateUtcToSecondsSinceEpoch(cls, utcDateTime: str):

        cutUtc = cls.dropUtcNanoseconds(utcDateTime)
        dateTime = cls.__convertUtcToDateTime(cutUtc)
        return cls.__translateDateTimeToSecondsSinceEpoch(dateTime)


    @classmethod
    def translateSecondsSinceEpochToUtc(cls, secondsSinceEpoch: float):

        return str(cls.__translateSecondsSinceEpochToDateTime(secondsSinceEpoch))


    @staticmethod
    def dropUtcNanoseconds(utcDateTime: str):

        dotIndex = utcDateTime.rfind('.')

        dataTime = utcDateTime[: dotIndex + 6 + 1]
        return dataTime


    @staticmethod
    def __convertUtcToDateTime(utcDateTime: str):

        return datetime.strptime(utcDateTime, '%Y-%m-%d %H:%M:%S.%f')


    @staticmethod
    def __translateSecondsSinceEpochToDateTime(secondsSinceEpoch: float):

        return datetime.fromtimestamp(secondsSinceEpoch).strftime('%Y-%m-%d %H:%M:%S.%f')


    @staticmethod
    def __translateDateTimeToSecondsSinceEpoch(dateTime: datetime):

        return time.mktime(dateTime.timetuple()) + dateTime.microsecond / 1e6