# Internal
from tests.fakes.fake_mavlink_packages import *
from src.mapper.mappers.record_mapper import RecordMapper, Record
from src.domain.wrappers.mavlink_package_wrapper import MavlinkPackageWrapper
# Python
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def Records(FakeAttitudePackages):

    record1 = Record()
    record1.pipeId = 1
    record1.utcTime = '2019-03-13 06:23:30.835208'
    record1.package = MavlinkPackageWrapper(FakeAttitudePackages[0])

    record2 = Record()
    record2.pipeId = 1
    record2.utcTime = '2019-03-13 06:23:31.036249'
    record2.package = MavlinkPackageWrapper(FakeAttitudePackages[1])

    return [record1, record2]


@pytest.mark.filterwarnings("ignore: DeprecationWarning")
def test_RecordMapper_findRecordForPipe(DatabaseConnection, Records, AttitudeMetadata, FakeAttitudePackages):

    mapper = RecordMapper(DatabaseConnection)
    mapper.metadata = AttitudeMetadata

    firstPipeRecords = mapper.findRecordsForPipe(1)

    assert firstPipeRecords == Records
