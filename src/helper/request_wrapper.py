from .dict_wrapper import *


class RequestWrapper(DictWrapper):

    def getAllParameters(self):
        return set(self.dictionary.keys())

