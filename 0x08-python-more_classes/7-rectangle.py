#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initilizing the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Delete the rectangle"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """width prop"""
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
        """height prop"""
        return self.__height

    @height.setter
    def height(self, height):
        """height settings"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """Return the rectangle strng"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += str(self.print_symbol) * self.width + '\n'
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """Return the rectangle representation"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def area(self):
        """Return the area rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2
