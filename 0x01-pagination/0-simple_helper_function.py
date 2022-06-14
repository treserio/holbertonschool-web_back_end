#!/usr/bin/env python3
''' Write a function named index_range that takes two integer arguments page
and page_size. The function should return a tuple of size two containing a
start index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters. '''
import typing as typ


def index_range(page: int, page_size: int) -> typ.Tuple[int, int]:
    ''' return a tuple of the start end ind '''
    return (page_size * page) - page_size, page_size * page
