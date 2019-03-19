from src.data_source.storage.storages.i_storage import *
# Internal
from src.common.settings import settings
from src.common.decorators import override, singleton
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

        MapperRegistry().connection = sqlite3.connect(settings.pathToDatabase)
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
    def findSessionsInsideTimestamp(self, includeIncompleteEntries: bool, interval: Interval = None):

        sessionMapper = MapperRegistry().getMapperFor(Session)

        sessions = sessionMapper.findInsideTimestamp(includeIncompleteEntries, interval)
        return sessions


    @override
    def findAllPipes(self):

        pipeMapper = MapperRegistry().getMapperFor(Pipe)

        pipes = pipeMapper.findAll()
        return pipes


    @override
    def findPipesForSessions(self, sessionsId):

        pipeMapper = MapperRegistry().getMapperFor(Pipe)

        pipes = pipeMapper.findPipesForSessions(sessionsId)
        return pipes


    @override
    def findRecordsForPipe(self, pipeId: int, interval: Interval = None):

        pipeMapper = MapperRegistry().getMapperFor(Pipe)
        pipe = pipeMapper.find(pipeId)[0]

        recordMapper = MapperRegistry().getMapperFor(Record)
        recordMapper.metaData = pipe.metaData

        recordMapper.createRecordView()

        records = recordMapper.findRecordsForPipe(pipeId, interval)
        return records
