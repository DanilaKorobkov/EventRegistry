# Internal
from tests.fakes.fake_mavlink_packages import *
from src.mapper.mappers.record_mapper import RecordMapper, Record
from src.domain.wrappers.mavlink_package_wrapper import MavlinkPackageWrapper
from src.helper.interval import Interval
from src.helper.time_point import Unit, TimePoint
# Python
import pytest
from src.helper.time_point import TimePoint, Unit

@pytest.fixture
def Records(AttitudePackage, SnsPackage, PilotPackage, CompassPackage):

    record1 = Record()
    record1.pipeId = 1
    record1.timePoint = TimePoint('2019-03-13 06:23:41.736037', Unit.Utc).transformTo(Unit.Second)
    record1.package = MavlinkPackageWrapper(AttitudePackage)

    record2 = Record()
    record2.pipeId = 2
    record2.timePoint = TimePoint('2019-03-13 06:23:41.537338', Unit.Utc).transformTo(Unit.Second)
    record2.package = MavlinkPackageWrapper(SnsPackage)

    record3 = Record()
    record3.pipeId = 3
    record3.timePoint = TimePoint('2019-03-13 07:21:18.538242', Unit.Utc).transformTo(Unit.Second)
    record3.package = MavlinkPackageWrapper(PilotPackage)

    record4 = Record()
    record4.pipeId = 4
    record4.timePoint = TimePoint('2019-03-13 07:21:18.338870', Unit.Utc).transformTo(Unit.Second)
    record4.package = MavlinkPackageWrapper(CompassPackage)

    return [record1, record2, record3, record4]


@pytest.mark.filterwarnings("ignore")
def test_RecordMapper_findRecordForPipe(DatabaseConnection, Records, AttitudeMetadata):

    mapper = RecordMapper(DatabaseConnection)
    mapper.createRecordView()
    mapper.metaData = AttitudeMetadata

    firstPipeRecords = mapper.findRecordsForPipe(1)

    assert firstPipeRecords == [Records[0]]


@pytest.mark.filterwarnings("ignore")
def test_RecordMapper_findRecordForPipeInInterval(DatabaseConnection, Records, AttitudeMetadata):

    mapper = RecordMapper(DatabaseConnection)
    mapper.createRecordView()
    mapper.metaData = AttitudeMetadata

    interval1 = Interval(TimePoint('2019-03-13 06:23:41.726037', Unit.Utc),
                        TimePoint('2019-03-13 06:23:41.746037', Unit.Utc))

    interval2 = Interval(TimePoint('2019-03-13 06:23:41.746037', Unit.Utc),
                        TimePoint('2019-03-13 06:23:41.756037', Unit.Utc))

    recordsInInterval1 = mapper.findRecordsForPipe(1, interval = interval1)
    recordsInInterval2 = mapper.findRecordsForPipe(1, interval = interval2)

    assert recordsInInterval1 == [Records[0]]
    assert recordsInInterval2 == []

