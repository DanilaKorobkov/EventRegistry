# Internal
from tests.fakes.fake_mavlink_packages import *
from src.mapper.mappers.record_mapper import RecordMapper, Record
from src.domain.wrappers.mavlink_package_wrapper import MavlinkPackageWrapper
# Python
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def Records(AttitudePackage, SnsPackage, PilotPackage, CompassPackage):

    record1 = Record()
    record1.pipeId = 1
    record1.utcTime = '2019-03-13 06:23:41.736037'
    record1.package = MavlinkPackageWrapper(AttitudePackage)

    record2 = Record()
    record2.pipeId = 2
    record2.utcTime = '2019-03-13 06:23:41.537338'
    record2.package = MavlinkPackageWrapper(SnsPackage)

    record3 = Record()
    record3.pipeId = 3
    record3.utcTime = '2019-03-13 07:21:18.538242'
    record3.package = MavlinkPackageWrapper(PilotPackage)

    record4 = Record()
    record4.pipeId = 4
    record4.utcTime = '2019-03-13 07:21:18.338870'
    record4.package = MavlinkPackageWrapper(CompassPackage)

    return [record1, record2, record3, record4]


@pytest.mark.filterwarnings("ignore")
def test_RecordMapper_findRecordForPipe(DatabaseConnection, Records, AttitudeMetadata):

    mapper = RecordMapper(DatabaseConnection)
    mapper.metadata = AttitudeMetadata

    firstPipeRecords = mapper.findRecordsForPipe(1)

    assert firstPipeRecords == [Records[0]]
