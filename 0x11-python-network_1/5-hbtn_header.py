#!/usr/bin/python3
"""
fetching a url then get request headers
url will be passed as argument
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
