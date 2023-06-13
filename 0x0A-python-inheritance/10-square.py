#!/usr/bin/python3

"""Defines a Square class inherit from Rectangle."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Create a square class"""
    
    def __init__(self, size):
        """override init method"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """adding own description in str"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the Square"""
        return self.__size ** 2
