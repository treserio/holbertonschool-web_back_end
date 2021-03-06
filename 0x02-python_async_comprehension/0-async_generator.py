#!/usr/bin/env python3
''' Write a coroutine called async_generator that takes no arguments. The
coroutine will loop 10 times, each time asynchronously wait 1 second, then
yield a random number between 0 and 10. Use the random module.  '''
import random
import asyncio
import typing as typ


async def async_generator() -> typ.Generator[float, None, None]:
    ''' yields 10 values with a 1 sec pause '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
