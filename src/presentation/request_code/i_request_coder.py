"""Json запрос может быть обернут внутрь BSON, HTTP или т.п.
IRequestCoder - интерфейс для преобразования запроса в этот вид и обратно"""

# Internal
from src.common.decorators import final
from src.helper.request_wrapper import RequestWrapper


class IRequestCoder:

    @final
    def decodeMultiple(self, requests):

        return [RequestWrapper(self.decodeSingle(request)) for request in requests]


    @final
    def encodeMultiple(self, objects):

        return [self.encodeSingle(obj) for obj in objects]


    def encodeSingle(self, obj):
        raise NotImplementedError


    def decodeSingle(self, request):
        raise NotImplementedError


