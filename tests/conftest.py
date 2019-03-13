# Internal
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


# @pytest.fixture(scope='class')
# def DatabaseConnection():
#
#     import sqlite3
#
#     con = sqlite3.connect(":memory:")
#     con.text_factory = bytes
#     cur = con.cursor()
#
#     createSession = "CREATE TABLE IF NOT EXISTS Session (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
#                     "Timestamp  INTEGER   NOT NULL, Unit FLOAT NOT NULL, OriginTime TIMESTAMP NOT NULL);"
#     cur.execute(createSession)
#
#     createPipe = "CREATE TABLE IF NOT EXISTS Pipe (Id INTEGER   PRIMARY KEY AUTOINCREMENT NOT NULL, " \
#                  "SessionId  INTEGER REFERENCES Session(Id), Path TEXT NOT NULL, MetaData BLOB);"
#     cur.execute(createPipe)
#
#     createRecord = "CREATE TABLE IF NOT EXISTS Record (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
#                    "PipeId INTEGER REFERENCES Pipe(Id), Timestamp  INTEGER   NOT NULL, SerialData BLOB);"
#     cur.execute(createRecord)
#
#     sessions = [(0, 1, '2001-01-01'),
#                 (0, 2, '2002-02-02')]
#     cur.executemany('INSERT INTO Session (Timestamp, Unit, OriginTime)  VALUES (?,?,?)', sessions)
#
#     pipes = [(1, '/11/12/', b'\x11\x11'),
#              (2, '/21/22/', b'\x22\x22')]
#     cur.executemany('INSERT INTO Pipe (SessionId, Path, MetaData)  VALUES (?,?,?)', pipes)
#
#     records = [(1, 2, b'\x11\x11'),
#                (1, 3, b'\x22\x22'),
#                (1, 4, b'\x22\x22'),
#                (1, 5, b'\x22\x22'),
#                (2, 0, b'\x22\x22'),
#                (2, 1, b'\x22\x22'),
#                (2, 2, b'\x22\x22')]
#     cur.executemany('INSERT INTO Record (PipeId, Timestamp, SerialData)  VALUES (?,?,?)', records)
#
#     con.commit()
#
#     yield con
#
#     con.close()



@pytest.fixture(scope='session')
def DatabaseConnection():

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

    pipes = [(1, '/uavs/Emulator/Attitude//', '<mavlink><version>3</version>  <dialect>0</dialect>  <enums><enum name="RELIABILITY">      <description>Data reliability.</description>      <entry name="RELIABILITY_FAILED" value="0">        <description>Data is reliabile.</description>      </entry>      <entry name="RELIABILITY_OK" value="1">        <description>Data is not reliabile.</description>      </entry>    </enum>    </enums><messages><message id="22" name="ATTITUDE">      <description>The attitude in the aeronautical frame (right-handed, Z-down, X-front, Y-right).</description>      <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>      <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>      <field name="roll" type="float" units="rad">Roll angle in radians (-pi..+pi)</field>      <field name="pitch" type="float" units="rad">Pitch angle in radians (-pi..+pi)</field>      <field name="yaw" type="float" units="rad">Yaw angle in radians (-pi..+pi)</field>    </message>    </messages></mavlink>'),
             (1, '/uavs/Emulator/SNS//', '<mavlink><version>3</version>  <dialect>0</dialect>  <enums><enum name="RELIABILITY">      <description>Data reliability.</description>      <entry name="RELIABILITY_FAILED" value="0">        <description>Data is reliabile.</description>      </entry>      <entry name="RELIABILITY_OK" value="1">        <description>Data is not reliabile.</description>      </entry>    </enum>    </enums><messages><message id="21" name="SNS">      <description>The satellite navigation system.</description>      <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot)</field>      <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>      <field name="time_sns" type="uint64_t" units="ms">Satellite timestamp</field>      <field name="latitude" type="int32_t" units="degE7">Latitude (WGS84, EGM96 ellipsoid)</field>      <field name="longitude" type="int32_t" units="degE7">Longitude (WGS84, EGM96 ellipsoid)</field>      <field name="altitude" type="int32_t" units="mm">Satellite AMSL altitude</field>      <field name="groundspeed" type="float" units="m/s">Current ground speed</field>      <field name="climb" type="float" units="m/s">Satellite climb</field>      <field name="course" type="float" units="rad">Course over ground (NOT heading, but direction of movement) in radians (0..+2pi)</field>    </message>    </messages></mavlink>'),
             (2, '/uavs/Emulator/Pilot//', '<mavlink><version>3</version>  <dialect>0</dialect>  <enums><enum name="RELIABILITY">      <description>Data reliability.</description>      <entry name="RELIABILITY_FAILED" value="0">        <description>Data is reliabile.</description>      </entry>      <entry name="RELIABILITY_OK" value="1">        <description>Data is not reliabile.</description>      </entry>    </enum>    </enums><messages><message id="24" name="PITOT">      <description>The pitot tube data.</description>      <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>      <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>      <field name="tas" type="float" units="m/s">Current true airspeed</field>      <field name="ias" type="float" units="m/s">Current indicated airspeed</field>      <field name="mach" type="float">Current Mach number</field>    </message>    </messages></mavlink>'),
             (2, '/uavs/Emulator/Compass//', '<mavlink><version>3</version>  <dialect>0</dialect>  <enums><enum name="RELIABILITY">      <description>Data reliability.</description>      <entry name="RELIABILITY_FAILED" value="0">        <description>Data is reliabile.</description>      </entry>      <entry name="RELIABILITY_OK" value="1">        <description>Data is not reliabile.</description>      </entry>    </enum>    </enums><messages><message id="25" name="COMPASS">      <description>The compass data.</description>      <field name="time_boot_ms" type="uint32_t" units="ms">Timestamp (time since system boot).</field>      <field display="bitmask" enum="RELIABILITY" name="reliability" print_format="0x%04x" type="uint8_t">Reliability</field>      <field name="mag_heading" type="float" units="rad">Current magnetic heading in radians (0..+2pi)</field>      <field name="true_heading" type="float" units="rad">Current true heading in radians (0..+2pi)</field>    </message>    </messages></mavlink>')]
    cur.executemany('INSERT INTO Pipe (SessionId, Path, MetaData)  VALUES (?,?,?)', pipes)

    records = [(1, 778056604382693, b'\x21\x06\x00\x00\x53\xaa\xac\x3a\x0f\x67\xf3\x3c\x8b\xb2\x7f\x3f\x50'),
               (1, 778056403341619, b'\x1d\x05\x00\x00\x74\xa5\x83\x3a\x46\x42\xeb\x3c\xcc\xaf\x7f\x3f\x50'),
               (1, 778056204035799, b'\x9b\x04\x00\x00\xc8\xf0\x4a\x3a\x46\x21\xf3\x3c\x34\xae\x7f\x3f\x50'),

               (2, 778056404239732, b'\xa5\x88\xb8\x75\x69\x01\x00\x00\x1c\x05\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x33\x00\x00\x00\xd3\x3b\x64\x3d\xc3\x66\xd0\xbc\xe1\x19\xa9\x40\xff'),
               (2, 778056204642113, b'\xdd\x87\xb8\x75\x69\x01\x00\x00\x9a\x04\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x35\x00\x00\x00\x1f\xae\xa3\x3c\x78\x94\x3b\xbb\x14\x1a\xa9\x40\xff'),
               (2, 778056004923373, b'\x16\x87\xb8\x75\x69\x01\x00\x00\x96\x03\x00\x00\x65\x4a\x4b\x21\x6e\x4a\x4c\x1d\x2c\x00\x00\x00\x00\x7e\x02\x3c\xe5\x4f\x73\x3d\x70\x1a\xa9\x40\xff'),

               (3, 781513205703960, b'\x1c\x05\x00\x00\x40\xce\x61\x3e\x85\x9c\x60\x3e\x96\xfb\x3c\x39\x6d'),
               (3, 781513005636374, b'\x9a\x04\x00\x00\xe3\xd0\x94\x3d\x65\x07\x94\x3d\x98\x18\x79\x38\x6d'),
               (3, 781512805114272, b'\x96\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x6e'),

               (4, 781513206315730, b'\x1c\x05\x00\x00\x19\x15\xb0\x40\xe1\x19\xa9\x40\xfd'),
               (4, 781513006331392, b'\x9a\x04\x00\x00\x4c\x15\xb0\x40\x14\x1a\xa9\x40\xfd'),
               (4, 781512805769602, b'\x96\x03\x00\x00\xa8\x15\xb0\x40\x70\x1a\xa9\x40\xfd')]
    cur.executemany('INSERT INTO Record (PipeId, Timestamp, SerialData)  VALUES (?,?,?)', records)

    con.commit()

    yield con

    con.close()


