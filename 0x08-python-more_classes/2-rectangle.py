#!/usr/bin/python3
"""
Module 2-rectangle.py
create a class represents rectangle
with width and height.
define width and height getters
"""


class Rectangle:
    """
    Represent a rectangle
    has a width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = w
    
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h
    
    def area(self):
        """
        get the rectangle area
        """
        return (self.__height * self.__width)
    
    def perimeter(self):
        """
        get the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            per = (self.__height * 2 + self.__width * 2)
            return per
