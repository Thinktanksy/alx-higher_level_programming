#!/usr/bin/python3

""" Class that inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ sub-class of BaseGeometry """

    def __init__(self, width, height):
        """ init rectangle """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ return the area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ prints rectangle description """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
