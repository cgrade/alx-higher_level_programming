#!/usr/bin/python3

""" A python script that uses urllib to query a url and return a response
"""
import urllib.request

if __name__ == "__main__":
    # URL to fetch
    url = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    # Fetch the URL and store the response
    with urllib.request.urlopen(url) as response:
        # Read the response body as bytes
        response_bytes = response.read()

        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(response_bytes), response_bytes,
                      response_bytes.decode('utf-8')))
