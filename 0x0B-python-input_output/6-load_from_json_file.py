#!/usr/bin/python3

"""Write a function that creates an Object from JSON """
import json


def load_from_json_file(filename):
    """create object from json"""
    with open(filename, mode="r", encoding="utf-8") as file:
        my_obj = json.load(file)
        return my_obj
