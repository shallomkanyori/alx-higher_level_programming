#!/usr/bin/python3
"""This module defines the MyInt class."""


class MyInt(int):
    """Represents a custom int class with == and != inverted."""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
