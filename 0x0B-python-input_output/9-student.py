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

    def to_json(self):
        """Returns the dictionary representation of the student."""
        return self.__dict__
