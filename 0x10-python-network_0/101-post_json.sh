#!/bin/bash
# A script that sends a json file via POST method in a curl statment
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" 

