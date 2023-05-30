#!/usr/bin/python3
'''
Define square class
with size att.
safe init
then calculate area
'''


class Square:
    """Sqaure clase with size safe from errors"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """calculate the square area"""
        return (self.__size ** 2)
