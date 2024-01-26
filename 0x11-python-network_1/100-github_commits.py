#!/usr/bin/python3
"""
interview task !
Please list 10 commits (from the most recent to oldest)
of the  by the 
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


from sys import argv
import requests

if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/{}/{}/commits/".format(argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
