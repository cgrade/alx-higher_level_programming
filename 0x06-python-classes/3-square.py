#!/usr/bin/python3
"""
A script that Defines a Class,
private instance attributes
and optional instantiations
"""


class Square:
    """ A Class that computes
    The Square of an int(obj)
    """
    def __init__(self, size=0):
        """Constructor of the Square Classe"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ compute the Area of the size"""
        return (size**2)
