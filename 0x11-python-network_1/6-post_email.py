#!/usr/bin/python3
"""
making post request with some ddata
(email), then print resonse
"""


import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    mail = argv[2]
    res = requests.post(url, data={'email': mail})
    print(res.text)
