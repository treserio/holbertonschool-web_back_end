#!/usr/bin/env python3
''' Create a class BasicCache that inherits from BaseCaching and is a caching
system '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' BaseCaching Class '''
    def __init__(self):
        ''' init super(), iterator, and order dictionary '''
        super().__init__()
        self.i = 0
        self.cache_order = {}

    def put(self, key, item):
        ''' assign self.cache_data item value for key '''
        if key and item:
            self.cache_data[key] = item
            self.cache_order[key] = self.i
            self.i += 1
        # print(self.cache_order)

    def get(self, key):
        ''' return '''
        if key and key in self.cache_data:
            return self.cache_data[key]
