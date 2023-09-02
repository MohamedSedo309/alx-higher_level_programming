#!/usr/bin/python3
"""
Send  POST request to http://0.0.0.0:5000/search_user
with a given letter
letter must be variable `q`.
If no letter is provided, send `q=""`
"""


import sys
import requests

if __name__ == "__main__":
    letter = ""
    if len(sys.argv) == 1:
        letter = argv[1]
    mmap = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=mmap)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
