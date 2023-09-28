#!/usr/bin/python3
"""This module contains the find_peak and find_peak_rec functions."""


def find_peak_rec(arr, start, end):
    """Recursively finds the peak in a list of unsorted integers.

    Args:
        arr (list of integers): the list of unsorted integers.
        start (int): the index at which to start searching.
        end (int): the index at which to stop searching.

    Returns: The index of the peak if found. -1 otherwise.
    """
    if start > end:
        return -1

    m = (start + end) // 2
    if ((m == 0 or arr[m - 1] <= arr[m]) and
            (m == len(arr) - 1 or arr[m + 1] <= arr[m])):
        return m

    # find peak in the right side of the list
    if m < len(arr) - 1 and arr[m + 1] > arr[m]:
        return find_peak_rec(arr, m + 1, end)

    return find_peak_rec(arr, start, m - 1)


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    if not list_of_integers:
        return None

    ind = find_peak_rec(list_of_integers, 0, len(list_of_integers) - 1)

    return list_of_integers[ind]
