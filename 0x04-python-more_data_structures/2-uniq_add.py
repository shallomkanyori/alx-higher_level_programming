#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Returns the sum of all unique integers in a list."""
    if my_list is not None:
        uniq_sum = 0
        for x in set(my_list):
            uniq_sum += x

        return uniq_sum
