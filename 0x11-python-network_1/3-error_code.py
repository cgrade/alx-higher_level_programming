#!/usr/bin/python3

"""A Script that takes ina url, sends a request to the url
   and display the body of hte repsones
"""

import urllib.parse
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
