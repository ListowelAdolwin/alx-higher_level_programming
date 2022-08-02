#!/usr/bin/python3
"""
Reading files

"""


def read_file(filename=""):
    """
    Read from a file and print it

    """
    with open("filename", "r", encoding = "utf-8") as f:
        text = f.read()
        print(text, end="")

read_file("filename")
