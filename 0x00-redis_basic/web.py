#!/usr/bin/env python3
''' get_page module, get page returns HTML content from url '''
import requests
import redis


def get_page(url: str) -> str:
    ''' return HTML from url, and also '''
    red = redis.Redis()
    red.incr(f'count:{url}')
    red.expire(f'count:{url}', 10)
    res = requests.get(url)
    return res.content
