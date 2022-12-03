#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)

    for i, e in enumerate(my_list):
        if i != idx:
            new_list.append(e)
        else:
            new_list.insert(idx, element)
    return (new_list)
