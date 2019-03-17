# Internal
from src.domain.mavlink.mavlink_package_generator import MavlinkPackageGenerator
# Python
import pytest

@pytest.fixture
def MavlinkPackageFactory():

    def Impl(Payload):

        gen = MavlinkPackageGenerator()

        metaData = Payload['metaData']
        data = Payload['data']

        payload = next(iter(data))

        gen.changeDialect(metaData)
        mavlinkPackage = gen.generatePackageFor(payload)

        return mavlinkPackage

    return Impl


@pytest.fixture
def MavlinkPackageChecker():

    def Impl(Package, Payload):

        params = Payload['data']
        payload = next(iter(params))

        expectedObject = params[payload]

        for parameterName in expectedObject.__dict__:
            assert getattr(Package, parameterName) == getattr(expectedObject, parameterName)

    return Impl



@pytest.mark.filterwarnings("ignore")
def test_generatePackageFor_AttitudePayload(MavlinkPackageFactory, MavlinkPackageChecker, AttitudePayload):

    package = MavlinkPackageFactory(AttitudePayload)
    MavlinkPackageChecker(package, AttitudePayload)


@pytest.mark.filterwarnings("ignore")
def test_generatePackageFor_SnsPayload(MavlinkPackageFactory, MavlinkPackageChecker, SnsPayload):

    package = MavlinkPackageFactory(SnsPayload)
    MavlinkPackageChecker(package, SnsPayload)


@pytest.mark.filterwarnings("ignore")
def test_generatePackageFor_PilotPayload(MavlinkPackageFactory, MavlinkPackageChecker, PilotPayload):

    package = MavlinkPackageFactory(PilotPayload)
    MavlinkPackageChecker(package, PilotPayload)


@pytest.mark.filterwarnings("ignore")
def test_generatePackageFor_CompassPayload(MavlinkPackageFactory, MavlinkPackageChecker, CompassPayload):

    package = MavlinkPackageFactory(CompassPayload)
    MavlinkPackageChecker(package, CompassPayload)
