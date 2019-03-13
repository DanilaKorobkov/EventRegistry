"""Декораторы"""

# Python
import inspect

def singleton(cls):
    """
    A singleton decorator. Returns a wrapper objects. A call on that object
    returns a single instance object of decorated class. Use the __wrapped__
    attribute to access decorated class directly in unit tests
    """
    return _SingletonWrapper(cls)


class _SingletonWrapper:
    """
    A singleton wrapper class. Its instances would be created
    for each decorated class.
    """

    def __init__(self, cls):
        self.__wrapped__ = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        """Returns a single instance of decorated class"""
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance


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