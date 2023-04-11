#!/usr/bin/python3

class BaseGeometry:
    """
    A class to represent a base geometry
    """

    def area(self):
        """
        Method to raise an exception when an area of the geometry is not defined.
        """
        raise Exception("area() is not implemented")
