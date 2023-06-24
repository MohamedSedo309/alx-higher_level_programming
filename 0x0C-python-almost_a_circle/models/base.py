#usr/bin/python3
"""models/base.py Module"""
import json
import os.path
import csv


class Base:
    """Base class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ Initializes new instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert list to json string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        mymap = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                mymap.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(mymap)

        with open(filename, 'w') as f:
            f.write(lists)
