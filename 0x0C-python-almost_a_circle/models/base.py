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

    @classmethod
    def save_to_file(cls, list_objs):
        """ save an object in a file """
        filename = "{}.json".format(cls.__name__)
        dictionary = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                dictionary.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(dictionary)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ json string to dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            rec = cls(10, 10)
        else:
            rec = cls(10)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """ Return list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        cls_list = cls.from_json_string(list_str)
        instances_list = []

        for index in range(len(cls_list)):
            instances_list.append(cls.create(**cls_list[index]))

        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ method to save a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            dic_keys = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            dic_keys = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    dic_keys[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(dic_keys[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ method loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_element in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_element):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        ins_list = []

        for index in range(len(matrix)):
            ins_list.append(cls.create(**matrix[index]))

        return ins_list
