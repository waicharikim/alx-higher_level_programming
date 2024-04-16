#!/usr/bin/python3
"""
save_to_json_file function definition
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function writes an object to a text file
    using a JSON representation
    """

    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
