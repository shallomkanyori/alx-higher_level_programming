#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    for i in range(1, x + 1):
        try:
            print("{:d}".format(my_list[i - 1]), end="")
            printed += 1
        except (TypeError, ValueError):
            continue

    print("")
    return printed
