#!/usr/bin/env python3
''' Create a class LFUCache that inherits from BaseCaching and is a caching
system '''
BasicCache = __import__('0-basic_cache').BasicCache


class LFUCache(BasicCache):
    ''' LFUCache, least recently used, Class '''
    def __init__(self):
        ''' init super(), iterator, and order dictionary '''
        super().__init__()
        self.lru_order = {}
        self.lru = 0
        self.lfu_order = {}

    def put(self, key, item):
        ''' redefining puts method to use FIFO to maintain MAX_ITEMS '''
        if len(self.cache_data) == self.MAX_ITEMS \
                and key not in self.cache_data:
            # print('lfu_order', self.lfu_order)
            lfu_list = [
                k for k, v in self.lfu_order.items()
                if v == min(self.lfu_order.values())
            ]
            # print('lfu_list', lfu_list)
            if len(lfu_list) > 1:
                # LRU method
                rmKey = min(self.lru_order, key=lambda k: self.lru_order[k])
                # print('rmKey', rmKey)
                if rmKey not in lfu_list:
                    lru_deletes = {
                        key: self.lru_order[key] for key in lfu_list
                    }
                    # print('lru_deletes', lru_deletes)
                    rmKey = min(lru_deletes, key=lambda k: lru_deletes[k])
                    # print('rmKey2', rmKey)
            else:
                rmKey = lfu_list[0]
            del self.cache_data[rmKey]
            print('DISCARD:', rmKey)
            del self.lru_order[rmKey]
            del self.lfu_order[rmKey]
        super().put(key, item)
        self.lru_order[key] = self.lru
        self.lru += 1
        # print('input key', key)
        if key in self.lfu_order:
            self.lfu_order[key] += 1
        else:
            self.lfu_order[key] = 0

    def get(self, key):
        ''' the least recently USED, put & get? '''
        if key and key in self.lru_order:
            self.lru_order[key] = self.lru
            self.lru += 1
        if key and key in self.lfu_order:
            self.lfu_order[key] += 1
        # print('get', key, 'lfu_order:', self.lfu_order)
        return super().get(key)
