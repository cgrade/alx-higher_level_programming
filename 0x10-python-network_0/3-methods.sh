#!/bin/bash
# A shell script that takes in url and display all the methods allowed by the server using `curl`
curl -siX OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
