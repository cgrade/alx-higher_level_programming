#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""

import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[1], sys.argv[2])
    req = requests.get(url)

    # loop through all the commits to print out the 1st 10 commits
    count = 0
    for i in req.json():
        if count == 10:
            break
        print('{}: {}'.format(i['sha'], i['commit']['author']['name']))
        count += 1
