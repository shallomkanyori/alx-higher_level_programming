#!/usr/bin/python3
"""This module defines the print_square function.

    Functions:

        print_square(size)"""


def print_square(size):
    """Prints a square of the given size with the character #.

        Args:
            size (int): the size of the square."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
