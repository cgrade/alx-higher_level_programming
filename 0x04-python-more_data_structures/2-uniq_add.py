#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    for element in my_list:
        if element not in newlist:
            newlist.append(element)
    res = 0
    for items in newlist:
        res += items
    return res
