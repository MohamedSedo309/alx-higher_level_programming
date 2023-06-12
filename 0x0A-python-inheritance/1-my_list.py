#!/usr/bin/python3

"""Defines a class MyList that inherits from list"""


class MyList(list):
    """creating class"""
    
    def print_sorted(self):
        """sort all list items in ascending order"""
        print(sorted(self))
