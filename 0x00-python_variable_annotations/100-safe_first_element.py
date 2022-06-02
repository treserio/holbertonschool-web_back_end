#!/usr/bin/env python3
''' Augment the following code with the correct duck-typed annotations '''
import typing


# The types of the elements of the input are not know
def safe_first_element(
        lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, None]:
    ''' return first item of sequence, or nothing '''
    if lst:
        return lst[0]
    else:
        return None
