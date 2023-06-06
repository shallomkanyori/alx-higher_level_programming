#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        code = ord(str[i])
        a_code = ord('a')

        if code >= a_code and code <= ord('z'):
            code = code - a_code + ord('A')
        print("{:c}".format(code), end="")

    print()
