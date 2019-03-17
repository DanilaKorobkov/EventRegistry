from .i_request_coder import *
# Internal
from src.common.decorators import override
# Python
import bson


class BsonRequestCoder(IRequestCoder):

    @override
    def encodeSingle(self, obj):

        return bson.dumps(obj)


    @override
    def decodeSingle (self, request):

        return bson.loads(request)
