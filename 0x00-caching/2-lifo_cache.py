#!/usr/bin/env python3
''' Create a class LIFOCache that inherits from BaseCaching and is a caching
system '''
BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BasicCache):
    ''' LIFOCache Class '''
    def __init__(self):
        ''' init with super() '''
        super().__init__()

    def put(self, key, item):
        ''' redefining puts method to use LIFO to maintain MAX_ITEMS '''
        if len(self.cache_data) == self.MAX_ITEMS \
                and key not in self.cache_data:
            rmKey = max(self.cache_order, key=lambda k: self.cache_order[k])
            del self.cache_data[rmKey]
            print('DISCARD:', rmKey)
            del self.cache_order[rmKey]
        super().put(key, item)
