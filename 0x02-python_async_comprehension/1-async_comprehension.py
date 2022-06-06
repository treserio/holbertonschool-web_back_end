#!/usr/bin/env python3
''' The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers. '''
import typing as typ
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typ.List[float]:
    ''' returns 10 random numbers from an async function '''
    return [num async for num in async_generator()]
