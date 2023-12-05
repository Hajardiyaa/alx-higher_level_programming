#!/usr/bin/python3
"""the rectangle class"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width prop fct"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width settings"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Height prop fct"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height settings"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
