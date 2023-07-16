#!/usr/bin/python3
"""This module defines the Base class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)
