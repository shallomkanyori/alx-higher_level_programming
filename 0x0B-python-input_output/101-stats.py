#!/usr/bin/python3
"""This module is a script that reads from stdin and computes metrics."""
import sys


if __name__ == "__main__":
    lines = 0
    total_size = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
             "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            words = line.split(" ")
            total_size += int(words[-1])
            codes[words[-2]] += 1

            lines += 1
            if lines % 10 == 0:
                print(f"File size: {total_size}")
                [print(f"{k}: {codes[k]}") for k in sorted(codes.keys())
                    if codes[k] != 0]

    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        [print(f"{k}: {codes[k]}") for k in sorted(codes.keys())
            if codes[k] != 0]
        raise
