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

    def update(self, *args, **kwargs):
        """ create update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
