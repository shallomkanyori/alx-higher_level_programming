#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple in list."""
    if not my_list:
        return 0

    wavg_num = 0
    wavg_den = 0

    for entry in my_list:
        wavg_num += entry[0] * entry[1]
        wavg_den += entry[1]

    return wavg_num / wavg_den
