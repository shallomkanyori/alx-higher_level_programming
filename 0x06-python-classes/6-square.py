#!/usr/bin/python3
"""This module defines the Square class"""


class Square():
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square.

        Args:
            size(int): the size of the square. Defaults to 0."""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: the position of the square.

        Raises:
            TypeError: if value is not a tuple of two positive integers."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the square at its position with the character #"""

        if self.size == 0:
            print("")
        else:
            print("\n" * self.position[1], end="")

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def area(self):
        """Returns the area of the square"""
        return self.size ** 2
