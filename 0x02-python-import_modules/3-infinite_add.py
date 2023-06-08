#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0
    args = sys.argv
    argc = len(args)

    for i in range(1, argc):
        result += int(args[i])

    print(result)
