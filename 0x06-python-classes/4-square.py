#!/usr/bin/python3
"""Defining a square class"""


class Square:
    """Square class. Has a size"""
    def __init__(self, size=0):
        """Initializing Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Return the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
