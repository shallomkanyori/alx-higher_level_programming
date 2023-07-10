#!/usr/bin/python3
"""This module defines the Rectangle class, a subclass of BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle."""

    def __init__(self, width, height):
        """Initializes the rectangle with a width and height.

            Args:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
