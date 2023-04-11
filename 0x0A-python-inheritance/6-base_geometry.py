#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """A class to represent a base geometry"""

    def area(self):
    """ Method to raise an exception when an area of the geometry is not defined."""
    raise Exception("area() is not implemented")
