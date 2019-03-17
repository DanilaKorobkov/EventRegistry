# Internal
from .bson_package_transformer import *


class PackageTransformerFactory:

    @classmethod
    def getPackageTransformer(cls):

        return cls.__getBsonPackageTransformer()


    @staticmethod
    def __getBsonPackageTransformer():
        return BsonPackageTransformer()