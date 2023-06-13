#!/usr/bin/python3

"""Defines a Square class inherit from Rectangle."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Create a square class"""
    
    def __init__(self, size):
        """override init method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
