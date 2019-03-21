# Internal
from src.common.project_paths import pathToRuntimeGeneratedDialects
from src.domain.mavlink.mavlink_dialect_generator import MavlinkDialectGenerator
# Python
import pytest


@pytest.fixture(params = [{'id': 22, 'struct': 'MAVLink_attitude_message'}, {'id': 24, 'struct': 'MAVLink_pilot_message'}])
def DataSet(request, AttitudeMetadata, PilotMetadata):

    data = request.param

    metaData = AttitudeMetadata if data['struct'] == 'MAVLink_attitude_message' else PilotMetadata
    data.update({'metaData': metaData.encode('utf-8')})

    return data


@pytest.mark.filterwarnings("ignore")
def test_MavlinkDialectGenerator_generateUsing(DataSet):

    mavlinkDialectGenerator = MavlinkDialectGenerator()

    module = mavlinkDialectGenerator.generateUsing(DataSet['metaData'])

    import sys

    sys.path.append(pathToRuntimeGeneratedDialects)
    module =  __import__(module, globals(), locals(), ['object'], 0)

    id = next(iter(module.mavlink_map))
    assert id == DataSet['id'] and module.mavlink_map[id].__name__ == DataSet['struct']
