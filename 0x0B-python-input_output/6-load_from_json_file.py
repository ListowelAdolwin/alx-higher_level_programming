#!/usr/bin/python3
"""
Create an object form a JSON file

"""


import json


def load_from_json_file(filename):
    """
    Creaete an object from filename

    """

    with open(filename, 'r') as f:
        return json.load(f)
