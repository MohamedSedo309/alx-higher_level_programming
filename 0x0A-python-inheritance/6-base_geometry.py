#!/usr/bin/python3

"""Write a class BaseGeometry
Public instance method: def area(self): that raises an Exception with the message area() is not implemented"""


class BaseGeometry:
    """creating empty class"""
    
    def area(self):
        """area exception function"""
        raise Exception("area() is not implemented")
