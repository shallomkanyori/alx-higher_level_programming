#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key-value pair in a dictionary."""
    if a_dictionary is not None and key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
