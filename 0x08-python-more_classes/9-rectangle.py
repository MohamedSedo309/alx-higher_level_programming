#!/usr/bin/python3
"""
Module 9-rectangle.py
create a class represents rectangle
with width and height.
define width and height getters
add __del__ function
add print symbol var
add compare function
"""


class Rectangle:
    """
    Represent a rectangle
    has a width and height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init function """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        
    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = w
    
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, h):
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = h
    
    def area(self):
        """
        get the rectangle area
        """
        return (self.__height * self.__width)
    
    def perimeter(self):
        """
        get the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            per = (self.__height * 2 + self.__width * 2)
            return per
    
    def __str__(self):
        """
        prints a rectangle of # char
        """
        w = self.__width
        h = self.__height
        if w == 0 or h == 0:
            return ""
        else:
            nstr = ""
            for i in range(h):
                for j in range(w):
                    nstr += str(Rectangle.print_symbol)
                if i != self.__height - 1:
                    nstr += "\n"
            return nstr
    
    def __repr__(self):
        """
        Return a string representation of
        the rectangle that can be used
        to recreate it
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
        
    def __del__(self):
        """an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on their area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_1 = rect_1.area()
            area_2 = rect_2.area()
            if area_1 >= area_2:
                return rect_1
            else:
                return rect_2
    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance 
        as square h = w = size
        """
        return cls(size, size)
