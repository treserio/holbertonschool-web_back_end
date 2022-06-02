#!/usr/bin/env python3
''' Use mypy to validate the following piece of code and apply any necessary
changes. '''
import typing as typ


def zoom_array(lst: typ.Tuple, factor: int = 2) -> typ.List:
    ''' correct typing challenge '''
    zoomed_in: typ.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
