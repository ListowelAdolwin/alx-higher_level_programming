#!/usr/bin/python3
"""
Return the JSON representation of a file

"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of
     my_obj
    """

    return json.dumps(my_obj)
