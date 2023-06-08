#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    argc = len(args) - 1

    ending = ":" if argc == 1 else ("s:" if argc > 0 else "s.")
    print("{:d} argument{:s}".format(argc, ending))

    for i in range(1, argc + 1):
        print("{:d}: {:s}".format(i, args[i]))
