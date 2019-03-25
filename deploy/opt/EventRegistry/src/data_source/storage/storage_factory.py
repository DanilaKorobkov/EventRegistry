# Internal
from .storages.i_storage import IStorage
from .storages.database_storage import DatabaseStorage


class StorageFactory:

    @classmethod
    def getStorage(cls) -> IStorage:

        return cls.__getDatabaseStorage()


    @staticmethod
    def __getDatabaseStorage():

        return DatabaseStorage()
