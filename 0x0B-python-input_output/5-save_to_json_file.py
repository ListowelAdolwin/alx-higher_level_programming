#!/usr/bin/python3
"""
Write an object to a text file
using JSON representation

"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes the representation of my_obj
    to filename

    """

    with open(filename, 'w+', encoding="utf-8") as f:
        json.dump(my_obj, f)
