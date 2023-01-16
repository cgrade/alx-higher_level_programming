#!/usr/bin/python3
"""A Module that contains a function that checks
the instance of an object
"""


def is_kind_of_class(obj, a_class):
    """A func that checks if an obj is an instance of a Classs
    @param:
        obj:        The object
        a_class:    The class to compare with
    Returns: bool
    """
    return (isinstance(obj, a_class))
