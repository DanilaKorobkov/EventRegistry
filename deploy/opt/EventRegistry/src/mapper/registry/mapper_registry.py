# Internal
from src.common.decorators import singleton


class AlreadyRegistered(Exception):
    pass


@singleton
class MapperRegistry:

    def __init__(self):

        self.mappers = {}
        self.__connection = None


    @property
    def connection(self):
        return self.__connection


    @connection.setter
    def connection(self, _connection):

        if not self.__connection:
            self.__connection = _connection

        else:
            import warnings
            warnings.warn('Connection will not change')



    def getMapperFor(self, classObject):

        return self.mappers.get(classObject, None)


    def setMapperFor(self, classObject, mapperClass):

        if self.getMapperFor(classObject) is None:

            mapper = mapperClass(self.connection)
            self.mappers.update({classObject: mapper})

        else:
            raise AlreadyRegistered(str(classObject), str(mapperClass))
