

class IPackageWrapper:

    def __init__(self, package):
        self.package = package


    def __getattr__(self, item):
        return getattr(self.package, item)


    def toDict(self):
        raise NotImplementedError
