#!/usr/bin/python3
"""This module is a script that reads stdin and computes metrics."""
import sys


def print_info(total_size, codes):
    """Prints metrics.

        Args:
            total_size (int): the total size of all files so far.
            codes (dict): the frequency count of the status codes.
    """
    print(f"File size: {total_size}")
    [print(f"{k}: {codes[k]}") for k in sorted(codes.keys()) if codes[k] != 0]


if __name__ == "__main__":
    lines = 0
    total_size = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
             "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            words = line.split()

            try:
                total_size += int(words[-1])
            except (IndexError, ValueError):
                pass

            try:
                codes[words[-2]] += 1
            except (KeyError, IndexError):
                pass

            lines += 1
            if lines % 10 == 0:
                print_info(total_size, codes)

        print_info(total_size, codes)

    except KeyboardInterrupt:
        print_info(total_size, codes)
        raise
