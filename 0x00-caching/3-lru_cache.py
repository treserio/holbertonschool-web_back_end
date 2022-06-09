#!/usr/bin/env python3
''' Create a class LRUCache that inherits from BaseCaching and is a caching
system '''
BasicCache = __import__('0-basic_cache').BasicCache


class LRUCache(BasicCache):
    ''' LRUCache, least recently used, Class '''
    def __init__(self):
        ''' init super(), iterator, and order dictionary '''
        super().__init__()
        self.lru_order = {}
        self.lru = 0

    def put(self, key, item):
        ''' redefining puts method to use FIFO to maintain MAX_ITEMS '''
        if len(self.cache_data) == self.MAX_ITEMS \
                and key not in self.cache_data:
            rmKey = min(self.lru_order, key=lambda k: self.lru_order[k])
            del self.cache_data[rmKey]
            print('DISCARD:', rmKey)
            del self.lru_order[rmKey]
        super().put(key, item)
        self.lru_order[key] = self.lru
        self.lru += 1

    def get(self, key):
        ''' the least recently USED, put & get? '''
        if key and key in self.lru_order:
            self.lru_order[key] = self.lru
            self.lru += 1
        return super().get(key)
