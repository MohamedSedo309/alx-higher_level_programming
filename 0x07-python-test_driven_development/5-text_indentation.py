#!/usr/bin/python3
"""
Module 5-text_indentation.py
Write a function that prints a text with 2 new 
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new 
    lines after each of ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    my_text = ""
    for char in text:
        if char in [".", "?", ":"]:
            my_text += char + "\n\n"
        else:
            my_text += char
    print(my_text)
