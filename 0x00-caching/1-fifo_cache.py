#!/usr/bin/env python3
''' Create a class FIFOCache that inherits from BaseCaching and is a caching
system '''
BasicCache = __import__('0-basic_cache').BasicCache


class FIFOCache(BasicCache):
    ''' FIFOCache Class '''
    def __init__(self):
        ''' init with super() '''
        super().__init__()

    def put(self, key, item):
        ''' redefining puts method to use FIFO to maintain MAX_ITEMS '''
        if len(self.cache_data) == self.MAX_ITEMS \
                and key not in self.cache_data:
            rmKey = min(self.cache_order, key=lambda k: self.cache_order[k])
            del self.cache_data[rmKey]
            print('DISCARD:', rmKey)
            del self.cache_order[rmKey]
        super().put(key, item)
