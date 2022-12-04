#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = list()
    if ((idx < 0) or (idx > (len(my_list)) - 1)):
        return (my_list)
    for i, e in enumerate(my_list):
        if i == idx:
            continue
        new_list.append(e)
    return (new_list)
