#!/usr/bin/python3
"""the rectangle class"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """Initilizes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, width):
        """width settings"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, height):
        """height settings"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Returning the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returning the perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2
