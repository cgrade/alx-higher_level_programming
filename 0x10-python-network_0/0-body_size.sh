#!/bin/bash
# A shell script that displays the size of the body response
curl -s "$1" | wc -c
