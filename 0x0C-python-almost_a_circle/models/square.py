#!/usr/bin/python3
"""This module defiens the Square class."""
from .rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square.

            Args:
                size (int): the size of the square.
                x (int): the x coordinate of the square.
                y (int): the y coordinate of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
