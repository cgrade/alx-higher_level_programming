#!/usr/bin/python3
"""A Script that defines a Class
with a private instance variable"""


class Square:
    """A Class that compute the square
    of integers"""

    def __init__(self, size):
        """Constructor of the Class Square"""
        self.__size = size
