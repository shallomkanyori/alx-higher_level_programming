#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns the length of sentence and its first character as a tuple"""
    res = (len(sentence), sentence[0] if sentence else "None")
    return res
