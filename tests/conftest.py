# Internal
from tests.domain.mavlink.conftest import *
from src.helper.dict_wrapper import DictWrapper
# Python
import pytest
from asyncio import coroutine
from unittest.mock import Mock


@pytest.fixture
def AsyncMock():

    def new():

        mock = Mock()
        mockFunc = Mock(side_effect=coroutine(mock))
        mockFunc.mock = mock

        return mockFunc

    return new


@pytest.fixture
def GetRequest():
    return DictWrapper({'type': 'get', 'data': {'what': 'Pipes', 'sessionsId': [], 'interval': {'startNanoseconds': 1, 'stopNanoseconds': 2}}})


@pytest.fixture
def SetRequest():
    return DictWrapper({'type': 'set', 'data': {}})


@pytest.fixture
def RequestWithWrongType():
    return DictWrapper({'type': 'Wrong', 'data': {}})


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

    records = [(1, 778056604382693, b'\x21\x06\x00\x00\x53\xaa\xac\x3a\x0f\x67\xf3\x3c\x8b\xb2\x7f\x3f\x50'),
               (1, 778056403341619, b'\x1d\x05\x00\x00\x74\xa5\x83\x3a\x46\x42\xeb\x3c\xcc\xaf\x7f\x3f\x50'),

               (2, 778056404239732, b'\xa5\x88\xb8\x75\x69\x01\x00\x00\x1c\x05\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x33\x00\x00\x00\xd3\x3b\x64\x3d\xc3\x66\xd0\xbc\xe1\x19\xa9\x40\xff'),
               (2, 778056204642113, b'\xdd\x87\xb8\x75\x69\x01\x00\x00\x9a\x04\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x35\x00\x00\x00\x1f\xae\xa3\x3c\x78\x94\x3b\xbb\x14\x1a\xa9\x40\xff'),

               (3, 781513205703960, b'\x1c\x05\x00\x00\x40\xce\x61\x3e\x85\x9c\x60\x3e\x96\xfb\x3c\x39\x6d'),
               (3, 781513005636374, b'\x9a\x04\x00\x00\xe3\xd0\x94\x3d\x65\x07\x94\x3d\x98\x18\x79\x38\x6d'),

               (4, 781513206315730, b'\x1c\x05\x00\x00\x19\x15\xb0\x40\xe1\x19\xa9\x40\xfd'),
               (4, 781513006331392, b'\x9a\x04\x00\x00\x4c\x15\xb0\x40\x14\x1a\xa9\x40\xfd')]
    cur.executemany('INSERT INTO Record (PipeId, Timestamp, SerialData)  VALUES (?,?,?)', records)

    con.commit()

    yield con

    con.close()


