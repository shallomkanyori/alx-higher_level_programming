#!/usr/bin/python3
"""This module defines the Rectangle class."""
from .base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle.

            Args:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.
                x (int): the x coordinate of the rectangle.
                y (int): the y coordinate of the rectangle.
                id (int): the id of the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """(int): the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """(int): the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """(int): the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """(int): the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
