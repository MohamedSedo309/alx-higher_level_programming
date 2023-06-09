#!/usr/bin/python3

"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """open the file then print its content"""
    with open(filename, encoding="utf-8") as file:
        text = file.read()
        print(text, end="")
