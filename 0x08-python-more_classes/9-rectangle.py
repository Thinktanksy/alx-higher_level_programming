#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """Rectangle class that defines a rectangle by its width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """String representation of Rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rec = ""
            for h in range(self.height):
                for w in range(self.width):
                    rec += str(self.print_symbol)
                if h < self.height - 1:
                    rec += "\n"
            return rec

    def __repr__(self):
        """Return string representation of Rectangle to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
