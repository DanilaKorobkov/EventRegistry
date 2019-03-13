from src.domain.converters.date_time_converter import DateTimeConverter


def test_DateTimeConverter_translateUtcToSecondsSinceEpoch():

    dateTime = '2019-03-13 13:53:01.633826'
    differentInMillisecondsDateTime = '2019-03-13 13:53:01.111111'

    secondsSinceEpoch = DateTimeConverter.translateUtcToSecondsSinceEpoch(dateTime)
    differentInMillisecondsSecondsSinceEpoch = DateTimeConverter.translateUtcToSecondsSinceEpoch(differentInMillisecondsDateTime)

    assert secondsSinceEpoch == 1552474381.633826
    assert differentInMillisecondsSecondsSinceEpoch != 1552474381.633826


def test_DateTimeConverter_translateSecondsSinceEpochToUtc():

    secondsSinceEpoch = 1552474381.6338258

    utc = DateTimeConverter.translateSecondsSinceEpochToUtc(secondsSinceEpoch)

    assert utc == '2019-03-13 13:53:01.633826'


def test_DateTimeConverter_dropUtcNanoseconds():

    utc = '2019-03-13 13:53:01.633826222'

    cutUtc = DateTimeConverter.dropUtcNanoseconds(utc)

    assert cutUtc == '2019-03-13 13:53:01.633826'