#!/usr/bin/python3

"""Write a function that writes a string to
a text file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        chars_count = file.write(text)
        return chars_count
