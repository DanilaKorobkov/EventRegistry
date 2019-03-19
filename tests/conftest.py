# Internal
from tests.domain.mavlink.conftest import *
from src.helper.request_wrapper import RequestWrapper
from src.helper.interval import Interval, TimePoint, Unit
# Python
import pytest
from asyncio import coroutine
from unittest.mock import Mock, MagicMock


@pytest.fixture
def AsyncMock():

    def new():

        mock = Mock()
        mockFunc = Mock(side_effect=coroutine(mock))
        mockFunc.mock = mock

        return mockFunc

    return new

@pytest.fixture(scope = 'module')
def SecondInterval():

    return Interval(TimePoint(1, Unit.Second),
                    TimePoint(2, Unit.Second))

# Supported request:
@pytest.fixture(scope = 'module')
def _GetAllSessionsRequestData():
    return RequestWrapper({'what': 'Sessions'})

@pytest.fixture(scope = 'module')
def GetAllSessionsRequest(_GetAllSessionsRequestData):
    return RequestWrapper({'type': 'get',
                           'data': _GetAllSessionsRequestData})


@pytest.fixture(scope = 'module')
def _GetSessionsInIntervalRequestData():
    return RequestWrapper({'what': 'Sessions',
                           'includeIncompleteEntries': False,
                           'interval': {'start': 1, 'stop': 2, 'unit': 'Second'}
                           })

@pytest.fixture(scope = 'module')
def GetSessionsInIntervalRequest(_GetSessionsInIntervalRequestData):
    return RequestWrapper({'type': 'get',
                           'data': _GetSessionsInIntervalRequestData})


@pytest.fixture(scope = 'module')
def _GetAllPipesRequestData():
    return RequestWrapper({'what': 'Pipes'})

@pytest.fixture(scope = 'module')
def GetAllPipesRequest(_GetAllPipesRequestData):
    return RequestWrapper({'type': 'get',
                           'data': _GetAllPipesRequestData})


@pytest.fixture(scope = 'module')
def _GetPipesForSessionsRequestData():
    return RequestWrapper({'what': 'Pipes',
                           'sessionsId': [1, 2]})

@pytest.fixture(scope = 'module')
def GetPipesForSessionsRequest(_GetPipesForSessionsRequestData):
    return RequestWrapper({'type': 'get',
                           'data': _GetPipesForSessionsRequestData})


@pytest.fixture(scope = 'module')
def _GetPipeRecordsRequestData():
    return RequestWrapper({'what': 'Records', 'pipeId': 1})

@pytest.fixture(scope = 'module')
def GetPipeRecordsRequest(_GetPipeRecordsRequestData):
    return RequestWrapper({'type': 'get',
                           'data':_GetPipeRecordsRequestData})


@pytest.fixture(scope = 'module')
def _GetPipeRecordsInIntervalRequestData():
    return RequestWrapper({'what': 'Records',
                           'pipeId': 1,
                           'interval': {'start': 1, 'stop': 2, 'unit': 'Second'}})

@pytest.fixture(scope = 'module')
def GetPipeRecordsInIntervalRequest(_GetPipeRecordsInIntervalRequestData):
    return RequestWrapper({'type': 'get',
                           'data': _GetPipeRecordsInIntervalRequestData})


# Invalid Requests:
@pytest.fixture
def RequestWithWrongFields():
    return RequestWrapper({'field1': 0,
                           'field2': 0})


@pytest.fixture
def _RequestWithWrongTypeData():
    return {}

@pytest.fixture
def RequestWithWrongType(_RequestWithWrongTypeData):
    return RequestWrapper({'type': 'Wrong',
                           'data': _RequestWithWrongTypeData})


@pytest.fixture(scope = 'module')
def _RequestWithoutWhatData():
    return {'field': 1}

@pytest.fixture(scope = 'module')
def RequestWithoutWhat(_RequestWithoutWhatData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithoutWhatData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidWhatData():
    return {'what': 'SessionRecordPipe'}

@pytest.fixture(scope = 'module')
def RequestWithInvalidWhat(_RequestWithInvalidWhatData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidWhatData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidFieldData():
    return {'what': 'SessionRecordPipe', 'field': 1}

@pytest.fixture(scope = 'module')
def RequestWithInvalidField(_RequestWithInvalidFieldData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidFieldData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidIncludeIncompleteEntriesTypeData():
    return {'what': 'Sessions',
            'includeIncompleteEntries': 2,
            'interval': {'start': 1, 'stop': 2, 'unit': 'Second'}}

@pytest.fixture(scope = 'module')
def RequestWithInvalidIncludeIncompleteEntriesType(_RequestWithInvalidIncludeIncompleteEntriesTypeData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidIncludeIncompleteEntriesTypeData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidFieldInIntervalData():
    return {'what': 'Sessions',
            'includeIncompleteEntries': 2,
            'interval': {'start': 1, 'stop': 2, 'unit': 'Second', 'field': 1}}

@pytest.fixture(scope = 'module')
def RequestWithInvalidFieldInInterval(_RequestWithInvalidFieldInIntervalData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidFieldInIntervalData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidIntervalStartTypeData():
    return {'what': 'Sessions',
            'includeIncompleteEntries': True,
            'interval': {'start': 'str', 'stop': 2, 'unit': 'Second'}}

@pytest.fixture(scope = 'module')
def RequestWithInvalidIntervalStartType(_RequestWithInvalidIntervalStartTypeData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidIntervalStartTypeData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidIntervalStopTypeData():
    return {'what': 'Sessions',
            'includeIncompleteEntries': True,
            'interval': {'start': 1, 'stop': 'str', 'unit': 'Second'}}

@pytest.fixture(scope = 'module')
def RequestWithInvalidIntervalStopType(_RequestWithInvalidIntervalStopTypeData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidIntervalStopTypeData})


@pytest.fixture(scope = 'module')
def _RequestWithInvalidIntervalUnitData():
    return {'what': 'Sessions',
            'includeIncompleteEntries': True,
            'interval': {'start': 1, 'stop': 'str', 'unit': 'str'}}

@pytest.fixture(scope = 'module')
def RequestWithInvalidIntervalUnit(_RequestWithInvalidIntervalUnitData):
    return RequestWrapper({'type': 'get',
                           'data': _RequestWithInvalidIntervalUnitData})


@pytest.fixture(scope = 'module')
def _PipesForSessionsRequestWithInvalidSessionsIdTypeData():
    return {'what': 'Pipes',
            'sessionsId': 1}

@pytest.fixture(scope = 'module')
def PipesForSessionsRequestWithInvalidSessionsIdType(_PipesForSessionsRequestWithInvalidSessionsIdTypeData):
    return RequestWrapper({'type': 'get',
                           'data': _PipesForSessionsRequestWithInvalidSessionsIdTypeData})


@pytest.fixture(scope = 'module')
def _PipesForSessionsRequestWithInvalidFieldData():
    return {'what': 'Pipes',
            'field': 1}

@pytest.fixture(scope = 'module')
def PipesForSessionsRequestWithInvalidField(_PipesForSessionsRequestWithInvalidFieldData):
    return RequestWrapper({'type': 'get',
                           'data': _PipesForSessionsRequestWithInvalidFieldData})


@pytest.fixture(scope = 'module')
def _PipeRecordsRequestWithWrongFieldData():
    return {'what': 'Records',
            'field': 1}

@pytest.fixture(scope = 'module')
def PipeRecordsRequestWithWrongField(_PipeRecordsRequestWithWrongFieldData):
    return RequestWrapper({'type': 'get',
                           'data': _PipeRecordsRequestWithWrongFieldData})


@pytest.fixture(scope = 'module')
def _PipeRecordsRequestWithWrongPipeIdTypeData():
    return {'what': 'Records',
            'pipeId': [1]}

@pytest.fixture(scope = 'module')
def PipeRecordsRequestWithWrongPipeIdType(_PipeRecordsRequestWithWrongPipeIdTypeData):
    return RequestWrapper({'type': 'get',
                           'data': _PipeRecordsRequestWithWrongPipeIdTypeData})


@pytest.fixture
def StorageMock():

    storage = MagicMock()

    storage.findAllSessions = MagicMock()
    storage.findRecordsForPipe = MagicMock()
    storage.findPipesForSessions = MagicMock()
    storage.findSessionsInsideTimestamp = MagicMock()

    return storage


@pytest.fixture(scope='session')
def DatabaseConnection(AttitudeMetadata, SnsMetadata, PilotMetadata, CompassMetadata):

    import sqlite3

    con = sqlite3.connect(":memory:")
    con.text_factory = bytes

    cur = con.cursor()

    createSession = "CREATE TABLE IF NOT EXISTS Session (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
                    "Timestamp  INTEGER   NOT NULL, Unit FLOAT NOT NULL, OriginTime TIMESTAMP NOT NULL);"
    cur.execute(createSession)


    createPipe = "CREATE TABLE IF NOT EXISTS Pipe (Id INTEGER   PRIMARY KEY AUTOINCREMENT NOT NULL, " \
                 "SessionId  INTEGER REFERENCES Session(Id), Path TEXT NOT NULL, MetaData BLOB);"
    cur.execute(createPipe)


    createRecord = "CREATE TABLE IF NOT EXISTS Record (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
                   "PipeId INTEGER REFERENCES Pipe(Id), Timestamp  INTEGER   NOT NULL, SerialData BLOB);"
    cur.execute(createRecord)


    sessions = [(778051053304369, 9.99999971718069e-10, '2019-03-13 06:23:36.386286716'),
                (781507268461814, 9.99999971718069e-10, '2019-03-13 07:21:12.601445377')]
    cur.executemany('INSERT INTO Session (Timestamp, Unit, OriginTime)  VALUES (?,?,?)', sessions)


    pipes = [(1, '/uavs/Emulator/Attitude//', AttitudeMetadata),
             (1, '/uavs/Emulator/SNS//', SnsMetadata),
             (2, '/uavs/Emulator/Pilot//', PilotMetadata),
             (2, '/uavs/Emulator/Compass//', CompassMetadata)]
    cur.executemany('INSERT INTO Pipe (SessionId, Path, MetaData)  VALUES (?,?,?)', pipes)


    records = [(1, 778056403341619, b'\x1d\x05\x00\x00\x74\xa5\x83\x3a\x46\x42\xeb\x3c\xcc\xaf\x7f\x3f\x50'),
               (2, 778056204642113, b'\xdd\x87\xb8\x75\x69\x01\x00\x00\x9a\x04\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x35\x00\x00\x00\x1f\xae\xa3\x3c\x78\x94\x3b\xbb\x14\x1a\xa9\x40\xff'),

               (3, 781513205703960, b'\x1c\x05\x00\x00\x40\xce\x61\x3e\x85\x9c\x60\x3e\x96\xfb\x3c\x39\x6d'),
               (4, 781513006331392, b'\x1c\x05\x00\x00\x19\x15\xb0\x40\xe1\x19\xa9\x40\xfd')]
    cur.executemany('INSERT INTO Record (PipeId, Timestamp, SerialData)  VALUES (?,?,?)', records)

    con.commit()

    yield con

    con.close()
