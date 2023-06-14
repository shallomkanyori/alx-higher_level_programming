#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if type(roman_string) != str:
        return 0

    digit_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}
    res = 0
    prev = 0

    for c in roman_string[::-1]:
        val = digit_map.get(c)
        res += -val if val < prev else val
        prev = val

    return res
