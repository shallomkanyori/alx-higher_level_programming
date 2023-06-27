#!/usr/bin/Python3
"""This module defines the MagicClass class"""
import math


class MagicClass():
    """Represents a circle"""

    def __init__(self, radius):
        """Initializes the circle.

        Args:
            radius (int or float): the radius of the circle."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of the circle"""
        return (2 * math.pi * self.__radius)
