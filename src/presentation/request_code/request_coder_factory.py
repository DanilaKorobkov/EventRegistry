# Internal
from .request_coders.i_request_coder import IRequestCoder
from .request_coders.bson_request_coder import BsonRequestCoder


class RequestCoderFactory:

    @classmethod
    def getRequestCoder(cls) -> IRequestCoder:

        return cls.__getBsonRequestCoder()


    @staticmethod
    def __getBsonRequestCoder():

        return BsonRequestCoder()
