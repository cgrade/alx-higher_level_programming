#!/usr/bin/python3
""" A script that takes in 2 args, an email address and a url
    it uses urllib to send a post request to the server
"""

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
