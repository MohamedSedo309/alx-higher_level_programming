#!/usr/bin/python3

"""create a class Student."""


class Student:
    """class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get Student to json """
        return self.__dict__
