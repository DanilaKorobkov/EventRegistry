

class DictWrapper:

    def __init__(self, dictonary):

        self.dictonary = dictonary


    def __getitem__(self, item):

        try:
            result = self.dictonary[item]

            if type(result) is dict:
                result = DictWrapper(result)

            return result

        except KeyError:
            return None


    def __setitem__(self, key, value):

        return self.dictonary.__setitem__(key, value)


    def __eq__(self, other):

        return self.dictonary == other
