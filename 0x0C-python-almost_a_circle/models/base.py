#usr/bin/python3
"""models/base.py Module"""


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
