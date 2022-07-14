#!/usr/bin/env python3
''' get_page module, get page returns HTML content from url '''
import requests
import redis


red = redis.Redis()


def get_page(url: str) -> str:
    ''' return HTML from url, and also'''
    red.incr(f'count:{url}')
    res = requests.get(url)
    return res.content
