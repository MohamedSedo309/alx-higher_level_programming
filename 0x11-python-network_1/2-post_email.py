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
<<<<<<< HEAD
    values = {'email': argv[2]}
=======
    value = {'email' : argv[2]}
>>>>>>> 91705af0d4d1212501a46c43b574a5c0735144c7
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
