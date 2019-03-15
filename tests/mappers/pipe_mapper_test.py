# Internal
from src.domain.objects.pipe import Pipe
from src.mapper.mappers.pipe_mapper import PipeMapper
# Python
import pytest


@pytest.fixture(scope = 'session')
def Pipes(AttitudeMetadata, SnsMetadata, PilotMetadata, CompassMetadata):

    pipe1 = Pipe()
    pipe1.path = ['uavs', 'Emulator', 'Attitude', '']
    pipe1.sessionId = 1
    pipe1.metaData = AttitudeMetadata

    pipe2 = Pipe()
    pipe2.path = ['uavs', 'Emulator', 'SNS', '']
    pipe2.sessionId = 1
    pipe2.metaData = SnsMetadata

    pipe3 = Pipe()
    pipe3.path = ['uavs', 'Emulator', 'Pilot', '']
    pipe3.sessionId = 2
    pipe3.metaData = PilotMetadata

    pipe4 = Pipe()
    pipe4.path = ['uavs', 'Emulator', 'Compass', '']
    pipe4.sessionId = 2
    pipe4.metaData = CompassMetadata

    return [pipe1, pipe2, pipe3, pipe4]


def test_PipeMapper_findAll(DatabaseConnection, Pipes):

    mapper = PipeMapper(DatabaseConnection)

    pipes = mapper.findAll()

    assert pipes == Pipes


def test_PipeMapper_findPipesForSessions(DatabaseConnection, Pipes):

    mapper = PipeMapper(DatabaseConnection)

    firstSessionPipe = mapper.findPipesForSessions([1])

    assert firstSessionPipe == [Pipes[0], Pipes[1]]


def test_PipeMapper_findPipesForSessionsInInterval(DatabaseConnection, Pipes):

    mapper = PipeMapper(DatabaseConnection)

    firstSessionPipe = mapper.findPipesForSessions([1])

    assert firstSessionPipe == [Pipes[0], Pipes[1]]
