#!/usr/bin/env python3
''' redis exercise module '''


import redis
import typing as typ
from uuid import uuid4
from functools import wraps


def count_calls(method: typ.Callable) -> typ.Callable:
    ''' return a wrapper to count the times a function is called '''
    meth_name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> typ.Union[int, str]:
        ''' wrapper to increment counter '''
        self._redis.incr(meth_name)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: typ.Callable) -> typ.Callable:
    ''' return a wrapper to store a functions arguments and output '''

    @wraps(method)
    def wrapper(self, *args) -> typ.Union[int, str]:
        ''' wrapper to store input/output history of a function '''
        meth_name = method.__qualname__
        self._redis.rpush(f"{meth_name}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{meth_name}:outputs", output)
        return output

    return wrapper


def replay(method: typ.Callable) -> None:
    ''' display the history of calls for a particular function '''
    Red = redis.Redis()
    qual = method.__qualname__
    # get a list of all the qual:inputs
    inputs = Red.lrange(f"{qual}:inputs", 0, -1)
    # get a list of all the qual:outputs
    outputs = Red.lrange(f"{qual}:outputs", 0, -1)
    print(f"{qual} was called {len(inputs)} times:")
    # print input and output sets decoded to utf-8
    print('\n'.join(
        f"{qual}(*{(i).decode('utf-8')}) -> {(o).decode('utf-8')}"
        for i, o in zip(inputs, outputs)
    ))


class Cache():
    ''' the cache class '''
    def __init__(self):
        ''' method for instanciating a Cache object '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
