#!/usr/bin/python3
"""
Creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """ Object from JSON file """
    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.load(f)
        return my_obj
