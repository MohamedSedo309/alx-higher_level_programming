#!/usr/bin/python3
"""
Using GitHub API to display a GitHub ID for user
creedintials passes as arguments
using Basic Authentication
"""


from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
