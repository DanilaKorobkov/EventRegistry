

class WrongRequest(Exception):
    pass


class IRequestHandler:

    def __init__(self, storage):

        self.storage = storage


    def handle(self, request):
        raise NotImplementedError
