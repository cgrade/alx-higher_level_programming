#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ A function that replaces all Occurences of an element
    by another in a new list"""
    new_list = my_list.copy()
    for index, element in enumerate(my_list):
        if element == search:
            new_list[index] = replace
    return (new_list)
