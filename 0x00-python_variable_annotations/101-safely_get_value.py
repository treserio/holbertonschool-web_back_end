#!/usr/bin/env python3
''' Given the parameters and the return values, add type annotations to the
function '''
import typing as typ


def safely_get_value(
    dct: typ.Mapping,
    key: typ.Any,
    default: typ.Union[typ.TypeVar('T'), None] = None
) -> typ.Union[typ.Any, typ.TypeVar('T')]:
    ''' gotta look into exactly what this function is doing '''
    if key in dct:
        return dct[key]
    else:
        return default
