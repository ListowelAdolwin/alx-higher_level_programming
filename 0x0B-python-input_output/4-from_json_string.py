#!/usr/bin/python3
"""
Returns an object represented by JSON

"""


import json


def from_json_string(my_str):
    """
    Return the object represented by my_str

    """

    return json.loads(my_str)
