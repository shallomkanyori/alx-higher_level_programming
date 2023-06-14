#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of element by another in a new list."""
    if my_list is not None:
        return [(replace if el == search else el) for el in my_list]
