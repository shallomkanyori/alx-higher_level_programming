#!/usr/bin/python3
"""This module defines the Rectangle class."""
from .base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle.

            All arguments other than 'id' are validated by the integer_validator
            function.

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
        self.integer_validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        """(int): the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        """(int): the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        """(int): the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value, True)
        self.__y = value

    def integer_validator(self, name, value, positive_0):
        """Validates integer attibutes.

            Args:
                name (str): the name of the attribute.
                value (int): the value of the attribute.
                positive_0 (bool): if True, consider 0 positive. Otherwise,
                                   don't consider 0 positive.

            Raises:
                TypeError: if value is not an integer.
                ValueError: if value is not positive.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if not positive_0 and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif positive_0 and value < 0:
            raise ValueError(f"{name} must be >= 0")
