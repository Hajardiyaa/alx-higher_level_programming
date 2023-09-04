#!/usr/bin/python3
"""Defining the square class"""


class Square:
     def __init__(self, size=0):
        """Initializing a new Square.


        Args:
        size (int): size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
