#usr/bin/python3
"""models/square.py Module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """square class inherit from rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """initializes new square"""
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """ str method """
        my_square = "[Square] "
        my_id = "({}) ".format(self.id)
        my_xy = "{}/{} - ".format(self.x, self.y)
        my_wh = "{}/{}".format(self.width, self.height)

        return my_square + my_id + my_xy + my_wh
        
        
    @property
    def size(self):
        """size getter"""
        return self.width
        
    @size.setter
    def size(self, value):
        """width setter"""
        self.width = value
        self.height = value
