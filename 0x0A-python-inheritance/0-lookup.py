#!/usr/bin/python3

"""
This module contains a function with the prototype:
def lookup(object)
and returns a list of the attributes of the object.
"""


def lookup(obj):
    """ A function that returns a list of attributes
    of an object
    @param: obj --> Object to lookup it's attributes
    Returns: List
    """
    return (dir(obj))
