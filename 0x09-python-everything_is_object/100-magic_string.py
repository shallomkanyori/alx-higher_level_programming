#!/usr/bin/python3
def magic_string():
    magic_string.arr = getattr(magic_string, "arr", []) + ["BestSchool"]
    return ", ".join(magic_string.arr)
