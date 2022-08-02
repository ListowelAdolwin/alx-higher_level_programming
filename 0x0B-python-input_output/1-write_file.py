#!/usr/bin/python3
"""
Write into into a file

"""


def write_file(filename="", text=""):
    """
    Write to a file and
    return the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        charNum = f.write(text)
        return charNum
