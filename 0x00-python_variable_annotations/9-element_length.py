#!/usr/bin/env python3
''' Annotate the below function's parameters and return values with the
appropriate types '''
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    ''' returns a list of tuples with their value & index from another list '''
    return [(i, len(i)) for i in lst]
