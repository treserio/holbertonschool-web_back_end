#!/usr/bin/env python3
''' get_page module, get page returns HTML content from url '''
import requests
import redis


def get_page(url: str) -> str:
    ''' return HTML from url, and also'''
    start = 0
    if not start:
        start += 1
        cnt = 0
    red = redis.Redis()
    cnt += 1
    red.set(f'count:{url}', cnt, 10)
    res = requests.get(url)
    return res.content
