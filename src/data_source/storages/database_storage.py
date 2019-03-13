from src.data_source.storages.i_storage import *
# Internal
from src.common.decorators import override, singleton, private
from src.mapper.registry.mapper_registry import MapperRegistry
from src.mapper.mappers.pipe_mapper import Pipe, PipeMapper
from src.mapper.mappers.record_mapper import Record, RecordMapper
from src.mapper.mappers.session_mapper import Session, SessionMapper
# Python
import sqlite3


@singleton
class DatabaseStorage(IStorage):

    def __init__(self):
        super().__init__()

        MapperRegistry().connection = sqlite3.connect('/tmp/pilotb_server')
        MapperRegistry().connection.text_factory = bytes

        MapperRegistry().setMapperFor(Pipe, PipeMapper)
        MapperRegistry().setMapperFor(Record, RecordMapper)
        MapperRegistry().setMapperFor(Session, SessionMapper)


    def __del__(self):

        MapperRegistry().connection.close()


    @override
    def findAllSessions(self):

        sessionMapper = MapperRegistry().getMapperFor(Session)
        sessions = sessionMapper.findAll()
        return sessions


    @override
    def findSessionsInsideTimestamp(self, parameters: dict):

        sessionMapper = MapperRegistry().getMapperFor(Session)
        sessions = sessionMapper.findInsideTimestamp(**parameters)
        return sessions


    @override
    def findAllPipes(self, includeRecords):

        pipeMapper = MapperRegistry().getMapperFor(Pipe)
        pipes = pipeMapper.findAll()

        if includeRecords:
            self.handleRecords(pipes)

        return pipes


    @override
    def findPipesForSessions(self, sessionsId, includeRecords):

        pipeMapper = MapperRegistry().getMapperFor(Pipe)
        pipes = pipeMapper.findPipesForSessions(sessionsId)

        if includeRecords:
            self.handleRecords(pipes)

        return pipes


    @private
    def handleRecords(self, pipes):

        recordMapper = MapperRegistry().getMapperFor(Record)

        for pipe in pipes:



            recordMapper.metadata = pipe.metaData
            pipe.records = recordMapper.findRecordsForPipe(pipe.primaryKey)
