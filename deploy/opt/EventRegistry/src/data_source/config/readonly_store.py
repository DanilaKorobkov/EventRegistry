# Internal
from src.common.decorators import private


class ReadOnlyStore:

    def __init__(self):

        self.__dict__ = self.getParameters()


    @private
    def getParameters(self) -> dict:
        raise NotImplementedError


    def __setattr__(self, key, value):

        if key == '__dict__' and not self.__dict__:
            object.__setattr__(self, key, value)

        else:
            raise AttributeError('Assign values to parameters in ReadonlyStore object is forbidden')