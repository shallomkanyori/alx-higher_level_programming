#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the largest integer value."""
    if a_dictionary:
        return max(a_dictionary, key=lambda k: a_dictionary[k])
