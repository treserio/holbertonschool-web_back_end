#!/usr/bin/env python3
''' Create a class MRUCache that inherits from BaseCaching and is a caching
system '''
BasicCache = __import__('0-basic_cache').BasicCache


class MRUCache(BasicCache):
    ''' MRUCache, least recently used, Class '''
    def __init__(self):
        ''' init super(), iterator, and order dictionary '''
        super().__init__()
        self.mru_order = {}
        self.mru = 0

    def put(self, key, item):
        ''' redefining puts method to use FIFO to maintain MAX_ITEMS '''
        if len(self.cache_data) == self.MAX_ITEMS \
                and key not in self.cache_data:
            rmKey = max(self.mru_order, key=lambda k: self.mru_order[k])
            del self.cache_data[rmKey]
            print('DISCARD:', rmKey)
            del self.mru_order[rmKey]
        super().put(key, item)
        self.mru_order[key] = self.mru
        self.mru += 1

    def get(self, key):
        ''' the least recently USED, put & get? '''
        if key and key in self.mru_order:
            self.mru_order[key] = self.mru
            self.mru += 1
        return super().get(key)
