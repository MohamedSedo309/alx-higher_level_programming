#!/usr/bin/python3
"""
Module 4-print_square.py
prints a square of # char
"""


def print_square(size):
    """
    prints a square of # char
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
