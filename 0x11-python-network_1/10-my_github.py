#!/usr/bin/python3
"""A script that takes your github credentials (username and password/PAT)
and uses the Github API to display user's ID
"""

import sys
import requests

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, passwd))
    print(req.json().get('id'))
