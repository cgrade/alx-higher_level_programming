#!/usr/bin/python3
"""A script that takes in a url args and returns a header info
   from that url
"""

import sys
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
