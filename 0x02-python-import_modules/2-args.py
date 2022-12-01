#!/usr/bin/python3
import sys

arg = sys.argv
arg_count = 0
num_of_arg = len(arg)
if arg_count < 1:
    print(f"{num_of_arg - 1} argument")
for i, item in enumerate(arg):
    print(f"{i}: {item}")

