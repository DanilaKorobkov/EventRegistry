# Internal
from src.common.settings import settings
from src.domain.event_registry import EventRegistry
from src.presentation.request_code.request_coder_factory import RequestCoderFactory
# Python
import zmq


class InputController:

    url = 'tcp://{ip}:{port}'.format(ip = settings.ip, 
                                     port = settings.port)

    def __init__(self):

        self.packageTransformer = RequestCoderFactory.getRequestCoder()

        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.REP)


    def start(self):

        self.socket.bind(self.url)
        self.startHandleIncomePackages()


    def startHandleIncomePackages(self):

        while True:

            try:
                self.__work()

            except Exception as exception:
                self.__handleException(exception)


    def __work(self):

        requests = self.socket.recv_multipart()
        requests = self.packageTransformer.decodeMultiple(requests)

        replies = EventRegistry().handleRequests(requests)
        replies = self.packageTransformer.encodeMultiple(replies)

        self.socket.send_multipart(replies)


    def __handleException(self, exception: Exception):

        reply = self.__wrapException(exception)
        reply = self.packageTransformer.encodeSingle(reply)

        self.socket.send_multipart([reply])


    @staticmethod
    def __wrapException(exception: Exception):

        return {'error': {'exception': exception.__class__.__name__, 'description': str(exception)}}
