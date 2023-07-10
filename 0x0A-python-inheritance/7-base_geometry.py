#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry():
    """Defines a geometry class."""

    def area(self):
        """A method that is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

            Args:
                name (str): the name of the value.
                value (int): the value.

            Raises:
                TypeError: if value is not an integer.
                ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
