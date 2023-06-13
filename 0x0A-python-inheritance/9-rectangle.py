#!/usr/bin/python3

"""Defines a Rectangle class inherit from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creating class and check the width and height value"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        
    def area(self):
        """override area function"""
        return self.__width * self.__height

    def __str__(self):
        """adding own description in str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
