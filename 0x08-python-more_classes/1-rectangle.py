#!/usr/bin/python3
"""This module defines the class Rectangle."""


class Rectangle():
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

            Args:
                width (int): the width of the rectangle,
                height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle.

            Raises:
                TypeError: if value is not an integer.
                ValueError: if value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle.

            Raises:
                TypeError: if value is not an integer.
                ValueError: if value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
