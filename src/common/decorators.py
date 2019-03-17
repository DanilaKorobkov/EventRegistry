"""Декораторы"""

# Python
import inspect


def override(func):
    return func


def final(func):
    return func


def private(func):

    def func_wrapper(*args, **kwargs):

        outer_frame = inspect.stack()[1][0]

        if 'self' not in outer_frame.f_locals or outer_frame.f_locals['self'] is not args[0]:
            raise Exception('Call private method: {}'.format(func.__name__))

        return func(*args, **kwargs)

    return func_wrapper


def singleton(cls):

    class _SingletonWrapper:

        def __init__(self, classObject):

            self.__wrapped__ = classObject
            self._instance = None


        def __call__(self, *args, **kwargs):

            if self._instance is None:
                self._instance = self.__wrapped__(*args, **kwargs)

            return self._instance

    return _SingletonWrapper(cls)
