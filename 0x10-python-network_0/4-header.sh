#!/bin/bash
# A script that uses curl to add a header variable and param to the query
curl "$1" -H "X-School-User-Id: 98"
