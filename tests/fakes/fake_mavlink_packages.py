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
def FakeAttitudePackages():
    package1 = FakeAttitudePackage(80, 1569, 0.9988180994987488, 0.02971222810447216, 0.0013173319166526198)
    package2 = FakeAttitudePackage(80, 1309, 0.9987761974334717, 0.028718125075101852, 0.0010043815709650517)

    return [package1, package2]


@pytest.fixture
def FakeSnsPackages():
    package1 = FakeSnsPackage(51, -0.02543962560594082, 5.284409046173096, 558582373, 491539053, 255, 1308,
                              1552458221733, 0.055721115320920944)
    package2 = FakeSnsPackage(53, -0.0028622429817914963, 5.284433364868164, 558582373, 491539053, 255, 1178,
                              1552458221533, 0.01998048834502697)

    return [package1, package2]


@pytest.fixture
def FakePilotPackages():
    package1 = FakePilotPackage(0.21934707462787628, 0.0001802280021365732, 109, 0.22051334381103516, 1308)
    package2 = FakePilotPackage(0.07227972894906998, 5.938913091085851e-05, 109, 0.0726640447974205, 1178)

    return [package1, package2]


@pytest.fixture
def FakeCompassPackages():
    package1 = FakeCompassPackage(5.502575397491455, 5.284409046173096, 253, 1308)
    package2 = FakeCompassPackage(5.502599716186523, 5.284433364868164, 253, 1178)

    return [package1, package2]


attitudePayloads = \
[
    {
        b'\x21\x06\x00\x00\x53\xaa\xac\x3a\x0f\x67\xf3\x3c\x8b\xb2\x7f\x3f\x50':
            FakeAttitudePackages()[0]
    },

    {
        b'\x1d\x05\x00\x00\x74\xa5\x83\x3a\x46\x42\xeb\x3c\xcc\xaf\x7f\x3f\x50':
            FakeAttitudePackages()[1]

    }
]

snsPayloads = \
[
    {
        b'\xa5\x88\xb8\x75\x69\x01\x00\x00\x1c\x05\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x33\x00\x00\x00\xd3\x3b\x64\x3d\xc3\x66\xd0\xbc\xe1\x19\xa9\x40\xff':
            FakeSnsPackages()[0]
    },

    {
        b'\xdd\x87\xb8\x75\x69\x01\x00\x00\x9a\x04\x00\x00\x65\x4a\x4b\x21\x6d\x4a\x4c\x1d\x35\x00\x00\x00\x1f\xae\xa3\x3c\x78\x94\x3b\xbb\x14\x1a\xa9\x40\xff':
            FakeSnsPackages()[1]
    }
]


pilotPayloads = \
[
    {
        b'\x1c\x05\x00\x00\x40\xce\x61\x3e\x85\x9c\x60\x3e\x96\xfb\x3c\x39\x6d':
            FakePilotPackages()[0]
    },

    {
        b'\x9a\x04\x00\x00\xe3\xd0\x94\x3d\x65\x07\x94\x3d\x98\x18\x79\x38\x6d':
            FakePilotPackages()[1]
    }
]


compassPayloads = \
[
    {
        b'\x1c\x05\x00\x00\x19\x15\xb0\x40\xe1\x19\xa9\x40\xfd':
            FakeCompassPackages()[0]
    },

    {
        b'\x9a\x04\x00\x00\x4c\x15\xb0\x40\x14\x1a\xa9\x40\xfd':
            FakeCompassPackages()[1]
    }
]