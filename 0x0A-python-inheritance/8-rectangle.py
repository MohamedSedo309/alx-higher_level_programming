#!/usr/bin/python3

"""Defines a Rectangle class inherit from BaseGeometry."""


class Rectangle(BaseGeometry):
    """creating class and check the width and height value"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
