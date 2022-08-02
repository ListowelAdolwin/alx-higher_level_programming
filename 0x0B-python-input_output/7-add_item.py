#!/usr/bin/python3
"""
This is the documentation for this module. On this file we have to
write a JSON rep of an object to a file

"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        import json
        text = json.dumps(my_obj)
        f.write(text)
