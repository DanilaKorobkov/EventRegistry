

class DictWrapper:

    def __init__(self, dictionary: dict):

        self.dictionary = dictionary


    def __getitem__(self, attributeName):

        value = None

        if self.hasAttribute(attributeName):

            value = self.dictionary.get(attributeName)

            if type(value) is dict:
                value = DictWrapper(value)

        return value


    def hasAttribute(self, attributeName):

        value = self.dictionary.get(attributeName, None)
        return value is not None


    def __setitem__(self, key, value):
        raise NotImplementedError


    def __eq__(self, other):
        return self.dictionary == other
