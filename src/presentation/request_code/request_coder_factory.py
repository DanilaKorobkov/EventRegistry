"""
Json запрос может быть обернут внутрь BSON, HTTP или т.п.
RequestCoderFactory - фабрика по созданию кодировщиков запросов
"""

# Internal
from .i_request_coder import IRequestCoder
from .bson_request_coder import BsonRequestCoder


class RequestCoderFactory:

    @classmethod
    def getRequestCoder(cls) -> IRequestCoder:

        return cls.__getBsonRequestCoder()


    @staticmethod
    def __getBsonRequestCoder():
        return BsonRequestCoder()