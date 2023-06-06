#!/usr/bin/python3
code_lower = ord('z')
code_upper = ord('Z')
for i in range(26):
    code = code_lower if i % 2 == 0 else code_upper
    print("{:c}".format(code), end="")
    code_lower = code_lower - 1
    code_upper = code_upper - 1
