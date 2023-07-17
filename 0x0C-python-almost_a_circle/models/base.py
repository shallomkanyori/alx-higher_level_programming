#!/usr/bin/python3
"""This module defines the Base class."""
import json
import csv


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
        except IOError:
            return []
        else:
            res = [cls.create(**d) for d in list_dicts]
            return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a csv file.

            Args:
                list_objs: the list of objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as cf:
            if not list_objs:
                cf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(cf, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a csv file and returns them in a lsit."""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as cf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                res_dicts = csv.DictReader(cf, fieldnames=fieldnames)
                res_dicts = [dict([k, int(v)] for k, v in d.items())
                             for d in res_dicts]

                return [cls.create(**d) for d in res_dicts]
        except IOError:
            return []
