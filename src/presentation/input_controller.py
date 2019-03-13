# Internal
from src.domain.event_registry import EventRegistry
from src.presentation.package_transformer.bson_package_transformer import BsonPackageTransformer
# Python
import zmq.asyncio
import asyncio


class InputController:

    url = 'tcp://127.0.0.1:4567'

    def __init__(self):

        self.packageTransformer = BsonPackageTransformer()

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

            print()
            requests = await self.socket.recv_multipart()
            print(requests)
            requests = self.packageTransformer.decodeMultiple(requests)
            print(requests[0].dictonary)
            replies = EventRegistry().handleRequests(requests)
            print(replies)
            replies = self.packageTransformer.encodeMultiple(replies)

            print(replies)
            print()
            await self.socket.send_multipart(replies)
            await asyncio.sleep(0)
