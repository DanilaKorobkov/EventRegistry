from .i_package_transformer import *
# Internal
from src.common.decorators import override
# Python
import bson


class BsonPackageTransformer(IPackageTransformer):

    @override
    def encodeSingle(self, obj):

        return bson.dumps(obj)


    @override
    def decodeSingle (self, request):

        return bson.loads(request)
