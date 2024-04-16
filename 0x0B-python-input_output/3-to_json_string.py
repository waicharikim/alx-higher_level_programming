#!/usr/bin/python3
"""
to_json_string function definition
"""

import json


def to_json_string(my_obj):
    """
    function returns the JSON representation of an
    object(string)
    """
    return json.dumps(my_obj)
