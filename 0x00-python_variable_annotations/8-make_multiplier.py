#!/usr/bin/env python3
''' Write a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float by
multiplier. '''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    ''' return a callable function to multiply a value by multiplier '''
    def return_funk(n: float) -> float:
        ''' return multiplier * n '''
        return n * multiplier
    return return_funk
