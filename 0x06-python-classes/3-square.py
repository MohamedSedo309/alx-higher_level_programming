#!/usr/bin/python3
"""
Define square class
with size att.
safe init
then calculate area
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side

    Functions:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            __size (int): default = 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates area for square

        Returns:
            area
        """
        return (self.__size)**2
