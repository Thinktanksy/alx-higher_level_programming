#!/usr/bin/python3
"""this module defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Calculator area """
        return super().area()

    def __str__(self):
        """ Print info """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    
