#!/usr/bin/python3
"""
Defines a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle
        Args:
            width(int): The width of the new Rectangle
            height(int): The height of the new Rectangle
            x(int): The x coordinate of the new Rectangle
            y(int): The y coordinate of the new Rectangle
            id(int): The identity of the new Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """
            Set/get the width of the Rectangle.
            """
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("Width must be an integer")
            if value < 0:
                raise ValueError("Width must be greater than 0")
            return self.__width = value

        @property
        def height(self):
            """
            Set/get the height of the Rectangle.
            """
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("Height must be an integer")
            if value < 0:
                raise ValueError("Height must be greater than 0")
            return self.__height = value

        @property
        def x(self):
            """
            Set/get the x coordinate of the Rectangle
            """
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("X must be an integer")
            if value < 0:
                raise ValueError("X must be greater than 0")
            return self.__x = value

        @property
        def y(self):
            """
            Set/get the y coordinate of the Rectangle
            """
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("Y must be an integer")
            if value < 0:
                raise ValueError("Y must be greater than 0")
            return self.__y = value
