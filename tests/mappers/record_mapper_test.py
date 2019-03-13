# Internal
from src.domain.objects.record import Record
from src.mapper.mappers.record_mapper import RecordMapper
# Python
import pytest


@pytest.fixture(scope = 'session')
def Records():

    p1Records = []

    for rec in [[1, 2, b'\x11\x11'],  [1, 3, b'\x22\x22'],  [1, 4, b'\x22\x22'], [1, 5, b'\x22\x22']]:

        record = Record()
        record.pipeId = rec[0]
        record.timeStamp = rec[1]
        record.serialData = rec[2]
        p1Records.append(record)


    p2Records = []

    for rec in [[2, 0, b'\x22\x22'],  [2, 1, b'\x22\x22'], [2, 2, b'\x22\x22']]:

        record = Record()
        record.pipeId = rec[0]
        record.timeStamp = rec[1]
        record.serialData = rec[2]
        p2Records.append(record)

    return [p1Records, p2Records]


@pytest.mark.xfail
def test_RecordMapper_findPipesForSessions(DatabaseConnection, Records):

    mapper = RecordMapper(DatabaseConnection)

    firstPipeRecords = mapper.findRecordsForPipe(1)

    assert firstPipeRecords == Records[0]


@pytest.mark.xfail
def test_RecordMapper_handleDataSet(DatabaseConnection, Records):

    mapper = RecordMapper(DatabaseConnection)

    pipe = mapper.handleDataSet((1, 1, 2, b'\x11\x11'))

    assert pipe == Records[0][0]

