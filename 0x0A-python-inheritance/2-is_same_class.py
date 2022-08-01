#!/usr/bin/python3
"""
A program to tell whether an object is
or not an instance of another

"""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an
    instance of another

    """
    if (isinstance(obj, a_class)):
        return True
    esle:
        return False
