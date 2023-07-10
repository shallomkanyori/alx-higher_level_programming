#!/usr/bin/python3
"""This module defines the Square class, a subclass of the Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size):
        """Initializes a square.

            Args:
                size (int): the size of the sqaure.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {0:d}/{0:d}".format(self.__size)
