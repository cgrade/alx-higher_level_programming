#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return (None)
    i = 0
    for m in my_list:
        if m > i:
            i = m
    return (i)
