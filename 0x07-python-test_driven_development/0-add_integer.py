#!/usr/bin/python3
"""
Module 0-add_integer
adds 2 ins or floats
"""


def add_integer(a, b=98):
    """
    Return sum of a + b int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b
