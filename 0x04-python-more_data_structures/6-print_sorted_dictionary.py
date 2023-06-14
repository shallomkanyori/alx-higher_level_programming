#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary ordered by its keys."""
    if a_dictionary is not None:
        for key in sorted(a_dictionary):
            print("{:s}: {}".format(key, a_dictionary[key]))
