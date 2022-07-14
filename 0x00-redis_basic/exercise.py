#!/usr/bin/env python3
''' redis exercise module '''


import redis
import typing as typ
from uuid import uuid4
from functools import wraps


def count_calls(method: typ.Callable) -> typ.Callable:
    ''' return the number of times a callable was called '''
    meth_name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> typ.Union[int, str]:
        ''' wrapper to increment counter '''
        self._redis.incr(meth_name)
        return method(self, *args, **kwargs)

    return wrapper


class Cache():
    ''' the cache class '''
    def __init__(self):
        ''' method for instanciating a Cache object '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: typ.Union[str, bytes, int, float]) -> str:
        ''' generate random key to store data with '''
        k = str(uuid4)
        self._redis.set(k, data)
        return k

    def get(self, key: str, fn: typ.Callable = None) -> typ.Union[str, int]:
        ''' return data from self._redis using key '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        ''' return str data from cache '''
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        ''' return int data from cache '''
        return self.get(key, int)
