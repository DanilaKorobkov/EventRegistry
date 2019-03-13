# Internal
from src.data_source.storages.database_storage import DatabaseStorage


class StorageFactory:

    @staticmethod
    def getDatabaseStorage():

        return DatabaseStorage()
