#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initialization of class
        Args:
            width (int): private width of Rectangle
            height (int): private height of Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
