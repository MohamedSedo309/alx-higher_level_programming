#!/usr/bin/python3
"""
fetch requests (get)
"""


import requests

if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
