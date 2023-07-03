#!/usr/bin/python3
"""This module defines the class Rectangle."""


class Rectangle():
    """Defines a rectangle.

        Attributes:
            number_of_instances (int): the number of current instances.
            print_symbol (obj): the symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

            Args:
                width (int): the width of the rectangle,
                height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        res = ""
        if self.width == 0 or self.height == 0:
            return res

        for _ in range(self.height):
            res += str(self.print_symbol) * self.width + "\n"

        res = res[:-1]
        return res

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """int: The width of the rectangle.

            Raises:
                TypeError: if value is not an integer.
                ValueError: if value is less than 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle.

            Raises:
                TypeError: if value is not an integer.
                ValueError: if value is less than 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectange."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)
