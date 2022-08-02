#!/usr/bin/python3
"""
Append to a file

"""


def append_write(filename="", text=""):
    """
    Append text to the end of
    a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        charNum = f.append(text)
