#!/bin/bash
# A script that uses curl to send a POST request to the server and displays the response to stdout
curl -d "email=test@gmail.com&subject='I will always be here for PLD'" "$1"
