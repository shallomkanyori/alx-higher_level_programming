#!/usr/bin/python3
"""This module defines the LockedClass class."""


class LockedClass():
    """This class prevents dynamic creation of most instance attributes.

    It prevents the dynamic creation of attributes that are not called
    first_name.
    """

    __slots__ = "first_name"
