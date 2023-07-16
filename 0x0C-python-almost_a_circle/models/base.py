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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of a list of objects to file.

            Args:
                list_objs: the list of objects.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []

        if list_objs:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())

        with open(filename, "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of a JSON string representation.

            Args:
                json_string (str): the JSON string representation.
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes set.

            Args:
                **dictionary: variable keyword arguments that are the
                              attributes of the instance to create.
        """
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        else:
            return

        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Returns a list of intances after loading them from a file."""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as f:
                list_dicts = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []
        else:
            res = []
            for d in list_dicts:
                res.append(cls.create(**d))

            return res
