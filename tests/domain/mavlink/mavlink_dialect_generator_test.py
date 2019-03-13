# Internal
from src.domain.mavlink.mavlink_dialect_generator import MavlinkDialectGenerator
# Python
import pytest


@pytest.fixture(params = [{'id': 21, 'struct': 'MAVLink_sns_message'}, {'id': 22, 'struct': 'MAVLink_attitude_message'}])
def DataSet(request, SnsMessageMetadata, AttitudeMessageMetadata):

    data = request.param

    metadata = SnsMessageMetadata if data['struct'] == 'MAVLink_sns_message' else AttitudeMessageMetadata
    data.update({'metadata': metadata})

    return data


@pytest.mark.filterwarnings("ignore: DeprecationWarning")
def test_MavlinkDialectGenerator_generateUsing(DataSet):

    mavlinkDialectGenerator = MavlinkDialectGenerator()

    module = mavlinkDialectGenerator.generateUsing(DataSet['metadata'])
    module =  __import__(module, globals(), locals(), ['object'], 0)

    id = next(iter(module.mavlink_map))
    assert id == DataSet['id'] and module.mavlink_map[id].__name__ == DataSet['struct']
