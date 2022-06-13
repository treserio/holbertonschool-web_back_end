#!/usr/bin/env python3
''' Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs:
    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation. '''
Server1 = __import__('1-simple_pagination').Server


class Server(Server1):
    ''' updated Server class with get_hyper method '''
    def __init__(self):
        ''' init from inherited class '''
        super().__init__()

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        ''' return requested dictionary item '''
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if (page + 1) * page_size
            < len(self.dataset()) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': -(-len(self.dataset()) // page_size),
        }
