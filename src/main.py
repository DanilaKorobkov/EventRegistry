# Internal
from src.presentation.input_controller import InputController
# Python
import asyncio


if __name__ == '__main__':

    inputController = InputController()

    loop = asyncio.get_event_loop()

    try:
        asyncio.ensure_future(inputController.start())
        loop.run_forever()

    finally:
        loop.close()
