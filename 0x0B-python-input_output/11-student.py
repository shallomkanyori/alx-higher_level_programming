#!/usr/bin/python3
"""This module defines the Student class."""


class Student():
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student.

            Args:
                first_name (str): the first name of the student.
                last_name (str): the last name of the student.
                age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the student.

            Args:
                attrs (list of str): the attributes to include. Defaults to
                None.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            res = {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            res = self.__dict__

        return res

    def reload_from_json(self, json):
        """Replaces all attributes of the student from a 'JSON' dictionary.

            Args:
                json: a dictionary containing the attributes to replace and
                    their values.
        """
        for key, val in json.items():
            setattr(self, key, val)
