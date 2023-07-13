#!/usr/bin/python3
"""This module defines the Base class."""


class Base():
    """The base class. Manages classes to avoid duplicating code."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance

            Args:
                id (int): the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
