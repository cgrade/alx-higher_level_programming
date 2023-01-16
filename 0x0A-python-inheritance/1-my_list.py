#!/usr/bin/python3

"""
This moddule contains a class definition that inherits
the list object, and has a sorted method
and all the elements must be and int.
"""


class Mylist(list):
    """A class that Inherit from list"""

    def print_sorted(self):
        """ A method that sort the elements of the list"""
        print(sorted(self))
