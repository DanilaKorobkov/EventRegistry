# Python
import pytest


class FakeAttitudePackage:

    def __init__(self, reliability, time_boot_ms, yaw, pitch, roll):

        self.yaw = yaw
        self.roll = roll
        self.pitch = pitch
        self.reliability = reliability
        self.time_boot_ms = time_boot_ms


class FakeSnsPackage:

    def __init__(self, altitude, climb, course, latitude, longitude, reliability, time_boot_ms, time_sns, groundspeed):

        self.altitude = altitude
        self.climb = climb
        self.course = course
        self.latitude = latitude
        self.longitude = longitude
        self.reliability = reliability
        self.time_boot_ms = time_boot_ms
        self.time_sns = time_sns
        self.groundspeed = groundspeed


class FakePilotPackage:

    def __init__(self, ias, mach, reliability, tas, time_boot_ms):

        self.ias = ias
        self.tas = tas
        self.mach = mach
        self.reliability = reliability
        self.time_boot_ms = time_boot_ms


class FakeCompassPackage:

    def __init__(self, mag_heading, true_heading, reliability, time_boot_ms):

        self.mag_heading = mag_heading
        self.true_heading = true_heading
        self.reliability = reliability
        self.time_boot_ms = time_boot_ms


@pytest.fixture
def AttitudePackage():

    package = FakeAttitudePackage(reliability = 80,
                                  time_boot_ms = 1309,
                                  yaw = 0.9987761974334717,
                                  pitch = 0.028718125075101852,
                                  roll = 0.0010043815709650517)
    return package


@pytest.fixture
def SnsPackage():

    package = FakeSnsPackage(altitude = 53,
                             climb = -0.0028622429817914963,
                             course = 5.284433364868164,
                             latitude = 558582373,
                             longitude = 491539053,
                             reliability = 255,
                             time_boot_ms = 1178,
                             time_sns = 1552458221533,
                             groundspeed = 0.01998048834502697)
    return package


@pytest.fixture
def PilotPackage():

    package = FakePilotPackage(ias = 0.21934707462787628,
                               mach = 0.0001802280021365732,
                               reliability = 109,
                               tas = 0.22051334381103516,
                               time_boot_ms = 1308)
    return package


@pytest.fixture
def CompassPackage():

    package = FakeCompassPackage(mag_heading = 5.502575397491455,
                                 true_heading = 5.284409046173096,
                                 reliability = 253,
                                 time_boot_ms = 1308)
    return package


attitudePayload = \
    {
        b'\x1d\x05\x00\x00\x74\xa5\x83\x3a\x46\x42\xeb\x3c\xcc\xaf\x7f\x3f\x50':
            AttitudePackage()
    }


snsPayload = \
    {
        b'\xdd\x87\xb8\x75\x69\x01\x00\x00\x9a\x04\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x35\x00\x00\x00\x1f\xae\xa3\x3c\x78\x94\x3b\xbb\x14\x1a\xa9\x40\xff':
        SnsPackage()
    }


pilotPayload = \
    {
        b'\x1c\x05\x00\x00\x40\xce\x61\x3e\x85\x9c\x60\x3e\x96\xfb\x3c\x39\x6d':
            PilotPackage()
    }

compassPayload = \
    {
        b'\x1c\x05\x00\x00\x19\x15\xb0\x40\xe1\x19\xa9\x40\xfd':
            CompassPackage()
    }
