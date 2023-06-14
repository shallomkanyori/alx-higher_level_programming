#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds a key-value pair in a dictionary."""
    if a_dictionary is not None:
        a_dictionary[key] = value

    return a_dictionary
