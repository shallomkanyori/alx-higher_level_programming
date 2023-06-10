#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        [print("{:d}".format(i)) for i in my_list[::-1]]
