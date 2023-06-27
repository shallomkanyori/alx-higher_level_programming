#!/usr/bin/python3
"""This module defines the Square class"""


class Square():
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size(int): the size of the square. Defaults to 0."""

        self.size = size

    @property
    def size(self):
        """int: the size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.size ** 2
