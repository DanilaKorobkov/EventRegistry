# Internal
from src.common.settings import settings
from src.domain.event_registry import EventRegistry
from src.presentation.request_code.request_coder_factory import RequestCoderFactory
# Python
import zmq.asyncio
import asyncio


class InputController:

    url = 'tcp://{ip}:{port}'.format(ip = settings.ip, 
                                     port = settings.port)

    def __init__(self):

        self.packageTransformer = RequestCoderFactory.getRequestCoder()

        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.REP)

        self.session = None


    def start(self):

        self.socket.bind(self.url)
        self.startHandleIncomePackages()


    async def stop(self):
        asyncio.ensure_future(self.stopImpl())


    async def stopImpl(self):

        self.session.cancel()
        self.session = None


    def startHandleIncomePackages(self):

        while True:

            print()
            requests = self.socket.recv_multipart()
            print(requests)
            requests = self.packageTransformer.decodeMultiple(requests)
            print(requests[0].dictionary)

            replies = EventRegistry().handleRequests(requests)
            print(replies)
            replies = self.packageTransformer.encodeMultiple(replies)
            print(replies)
            self.socket.send_multipart(replies)
            print()
            # await asyncio.sleep(0)
