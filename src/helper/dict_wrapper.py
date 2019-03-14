

class DictWrapper:

    def __init__(self, dictionary: dict):

        self.dictionary = dictionary


    def hasAttribute(self, name):

        value = self.dictionary.get(name, None)
        return value is not None


    def getAttribute(self, name):

        value = None

        if self.hasAttribute(name):

            value = self.dictionary.get(name)

            if type(value) is dict:
                value = DictWrapper(value)

        return value


    def __eq__(self, other):
        return self.dictionary == other
