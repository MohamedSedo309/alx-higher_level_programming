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
    values = {'email' : argv[2]}
    json = urllib.parse.urlencode(values)
    json = json.encode('ascii')
    request = urllib.request.Request(url, json)
    with urllib.request.urlopen(request) as response:
        print(respone.read().decode('utf-8'))
