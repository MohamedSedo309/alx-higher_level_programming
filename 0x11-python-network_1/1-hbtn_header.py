#!/usr/bin/python3
"""
fetch url and get reponse header
url is a parameter
"""


from sys import argv
import urllib.request

if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
