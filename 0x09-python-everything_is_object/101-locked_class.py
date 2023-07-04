#!/usr/bin/python3
"""This module defines the LockedClass class."""


class LockedClass():
    """This class prevents dynamic creation of most instance attributes.

    It prevents the dynamic creation of attributes that are not called
    first_name.
    """

    def __setattr__(self, key, value):
        if key != "first_name":
            err_msg = "'{}' object has no attribute '{}'".format(
                    type(self).__name__, key)
            raise AttributeError(err_msg)

        self.__dict__[key] = value
