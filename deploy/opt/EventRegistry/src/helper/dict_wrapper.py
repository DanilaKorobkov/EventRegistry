

class DictWrapper:

    def __init__(self, dictionary: dict):

        self.dictionary = dictionary


    def has(self, name):

        value = self.dictionary.get(name, None)
        return value is not None


    def get(self, name):

        value = None

        if self.has(name):

            value = self.dictionary.get(name)

            if type(value) is dict:
                value = self.__class__(value)

        return value


    def __eq__(self, other):
        return self.dictionary == other


    def __str__(self):
        return str(self.dictionary)
