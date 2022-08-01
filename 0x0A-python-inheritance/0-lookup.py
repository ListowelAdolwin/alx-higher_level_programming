#!/usr/bin/python3
"""
A program with just one function

"""


def lookup(obj):
    """
    A function that returns the available attributes
    and methods of an object

    """
    my_list = dir(obj)
    return my_list
