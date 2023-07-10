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
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
