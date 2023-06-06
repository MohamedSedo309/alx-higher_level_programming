#!/usr/bin/python3
"""
Module 3-say_my_name.py
Write a function that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    devide every item in all matrix by div
    Return: new matrix
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    full_name = first_name.strip() + " " + last_name.strip()
    print("My name is", full_name)
