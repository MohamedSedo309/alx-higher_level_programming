#!/usr/bin/python3
"""
adding some attr to the response
sending post request to url , with email data
"""


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    value = {'email' : argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
