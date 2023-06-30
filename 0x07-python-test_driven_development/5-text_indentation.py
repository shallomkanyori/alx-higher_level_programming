#!/usr/bin/python3
"""This module defines the text_indentation function.

    Functions:

        text_indentation(text)"""


def text_indentation(text):
    """Prints text with 2 newlines after these characters: [.?:].

        Args:
            text (str): the text to indent."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ind = 0
    for i in range(len(text)):
        if text[i] in '.?:':
            line = text[ind:i + 1].strip()
            print(line, end="\n\n")
            ind = i + 1

    if ind < len(text):
        line = text[ind:].strip()
        print(line, end="")
