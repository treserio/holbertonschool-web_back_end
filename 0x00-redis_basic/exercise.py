#!/usr/bin/env python3
''' redis exercise module '''


import redis
import typing as typ
from uuid import uuid4


class Cache():
    ''' the cache class '''
    def __init__(self):
        ''' method for instanciating a Cache object '''
        self._redis = redis.Redis()
        self._redis.flushdb()

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
