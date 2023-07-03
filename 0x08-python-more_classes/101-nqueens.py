#!/usr/bin/python3
"""This module prints every possible solution to the NQueen problem."""
import sys


def queens(n, i, a, b, c):
    """Generates solutions for the NQueen problem.

        Args:
            n (int): the number of queens to place.
            i (int): the current row.
            a (list of ints): the unavailable columns up-down
            b (list of ints): the unavailable columns diagonal up-right
            c (list of ints): the unavailable columns diagonal up-left
    """
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i + 1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


def main():
    """Finds and prints every possible solution to the NQueen problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in queens(n, 0, [], [], []):
        solution_b = [[i, j] for i, j in enumerate(solution)]
        print(solution_b)


if __name__ == "__main__":
    main()
