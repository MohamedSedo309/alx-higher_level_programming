#!/usr/bin/python3

"""Write a function that appends a string at the end of
a text file (UTF8) and returns the number of characters added"""


def write_file(filename="", text=""):
    """append text to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        chars_count = file.write(text)
        return chars_count
