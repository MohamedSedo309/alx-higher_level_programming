#usr/bin/python3
"""models/rectangle.py Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
    @property
    def width(self):
        """width getter"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        """height getter"""
        return self.__height
        
    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """find rectangle area"""
        return self.width * self.height

    def display(self):
        """prints a number of # that represent rectangle"""
        rec = self.y * "\n"
        for i in range(self.height):
            rec += (" " * self.x)
            rec += ("#" * self.width) + "\n"
        print(rec, end='')

    def __str__(self):
        """str method"""
        my_rec = "[Rectangle] "
        my_id = "({}) ".format(self.id)
        my_xy = "{}/{} - ".format(self.x, self.y)
        my_wh = "{}/{}".format(self.width, self.height)
        
        return my_rec + my_id + my_xy + my_wh

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
