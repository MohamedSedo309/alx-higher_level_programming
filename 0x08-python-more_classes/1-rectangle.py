#!/usr/bin/python3
"""
Module 1-rectangle.py
create a class represents rectangle
with width and height
"""


class Rectangle:
    """
    Represent a rectangle
    has a width and height
    """
    
    def __init__(self, width=0, height=0):
        """
        the init function
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """set rectangle width"""
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
        """set rectangle height"""
        return self.__height
        
    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h
