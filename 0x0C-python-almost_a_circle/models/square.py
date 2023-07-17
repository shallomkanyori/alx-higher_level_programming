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

    @property
    def size(self):
        """(int): the size of the square.

            Sets the width and height attributes to value.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

            Args:
                *args: valiable list of attribute values to update in the
                       order of id, size, x, y.
                **kwargs: variable dictionary of attributes to update and
                          their values.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]

            for i, val in enumerate(args):
                if i < 4:
                    setattr(self, attrs[i], val)
                else:
                    break

        elif kwargs:
            for attr, val in kwargs.items():
                if (attr == "id" and val is None):
                    self.__init__(self.size, self.x, self.y)
                elif attr in ["id", "size", "x", "y"]:
                    setattr(self, attr, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""

        res = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return res
