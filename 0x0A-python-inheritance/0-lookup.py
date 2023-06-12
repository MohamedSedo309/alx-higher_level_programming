#!/usr/bin/python3

"""Write a function that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """Return a list of object's attributes"""
    return (dir(obj))
