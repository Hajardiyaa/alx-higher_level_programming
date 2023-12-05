#!/usr/bin/python3
"""class rectangle"""
class Rectangle:
    def __init__(self, width=0, height=0):
"""initializtion"""
        self.width = width
        self.height = height

    @property
    def width(self):
"""prop fct"""
        return self.__width

    @width.setter
    def width(self, value):
"""width settings"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
"""prop fct"""
        return self.__height

    @height.setter
    def height(self, value):
"""heightsettings"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

