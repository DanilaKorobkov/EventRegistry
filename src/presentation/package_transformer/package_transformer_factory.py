# Internal
from .i_package_transformer import IPackageTransformer
from .bson_package_transformer import BsonPackageTransformer


class PackageTransformerFactory:

    @classmethod
    def getPackageTransformer(cls) -> IPackageTransformer:

        return cls.__getBsonPackageTransformer()


    @staticmethod
    def __getBsonPackageTransformer():
        return BsonPackageTransformer()