"""InputController - принимает запрос, раскодирует, делегирует обработку,
 кодирует и отправляет ответ"""

# Internal
from src.domain.event_registry import EventRegistry
from src.presentation.request_code.request_coder_factory import RequestCoderFactory
# Python
import zmq.asyncio
import asyncio


class InputController:

    url = 'tcp://127.0.0.1:4567'

    def __init__(self):

        self.packageTransformer = RequestCoderFactory.getRequestCoder()

        self.ctx = zmq.asyncio.Context()
        self.socket = self.ctx.socket(zmq.REP)

        self.session = None


    async def start(self):

        self.socket.bind(self.url)
        self.session = asyncio.ensure_future(self.startHandleIncomePackages())


    async def stop(self):
        asyncio.ensure_future(self.stopImpl())


    async def stopImpl(self):

        self.session.cancel()
        self.session = None


    async def startHandleIncomePackages(self):

        while self.session:

            requests = await self.socket.recv_multipart()
            requests = self.packageTransformer.decodeMultiple(requests)

            replies = EventRegistry().handleRequests(requests)
            replies = self.packageTransformer.encodeMultiple(replies)

            await self.socket.send_multipart(replies)
            await asyncio.sleep(0)
