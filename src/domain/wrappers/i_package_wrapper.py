

class IPackageWrapper:

    def __init__(self, package):
        self.package = package


    def toDict(self):
        raise NotImplementedError

