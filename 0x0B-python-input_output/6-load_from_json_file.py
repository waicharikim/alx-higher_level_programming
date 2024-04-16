#!/usr/bin/python3
"""
load_from_json_file function definition
"""

import json


def load_from_json_file(filename):
    """
    function creates an object from a
    JSON file
    """
    with open(filename, 'r') as f:
        return json.load(f)
