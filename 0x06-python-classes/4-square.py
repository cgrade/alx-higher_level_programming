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
        self.size = size

    def area(self):
        """ compute the Area of the size"""
        return (self.__size**2)

    @property
    def size(self):
        """getter"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
