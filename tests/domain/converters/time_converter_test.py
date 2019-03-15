from src.domain.converters.date_time_converter import DateTimeConverter


def test_DateTimeConverter_translateUtcToSecondsSinceEpoch():

    dateTime = '2019-03-13 13:53:01.633826'
    differentInMillisecondsDateTime = '2019-03-13 13:53:01.111111'

    secondsSinceEpoch = DateTimeConverter.translateUtcToSecondsSinceEpoch(dateTime)
    differentInMillisecondsSecondsSinceEpoch = DateTimeConverter.translateUtcToSecondsSinceEpoch(differentInMillisecondsDateTime)

    assert secondsSinceEpoch == 1552474381.633826
    assert differentInMillisecondsSecondsSinceEpoch != 1552474381.633826


def test_DateTimeConverter_translateSecondsSinceEpochToUtc():

    secondsSinceEpoch = 1552474381.633
    secondsSinceEpochWithMicroSec = 1552474381.633111
    secondsSinceEpochWithNanoSec = 1552474381.633111111

    utc = DateTimeConverter.translateSecondsSinceEpochToUtc(secondsSinceEpoch)
    utc2 = DateTimeConverter.translateSecondsSinceEpochToUtc(secondsSinceEpochWithMicroSec)
    utc3 = DateTimeConverter.translateSecondsSinceEpochToUtc(secondsSinceEpochWithNanoSec)

    assert utc == '2019-03-13 13:53:01.633000'
    assert utc2 == '2019-03-13 13:53:01.633111'
    assert utc3 == '2019-03-13 13:53:01.633111'


def test_DateTimeConverter_dropUtcNanoseconds():

    utc = '2019-03-13 13:53:01.633826222'
    utc2 = '2019-03-13 13:53:01.633826'
    utc3 = '2019-03-13 13:53:01.633'

    cutUtc = DateTimeConverter.dropUtcNanoseconds(utc)
    cutUtc2 = DateTimeConverter.dropUtcNanoseconds(utc2)
    cutUtc3 = DateTimeConverter.dropUtcNanoseconds(utc3)

    assert cutUtc == '2019-03-13 13:53:01.633826'
    assert cutUtc2 == '2019-03-13 13:53:01.633826'
    assert cutUtc3 == '2019-03-13 13:53:01.633'