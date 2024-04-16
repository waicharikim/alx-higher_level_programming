#!/usr/bin/python3
"""
from_json_string function definition
"""

import json


def from_json_string(my_str):
    """
    function returns an object represented by
    a JSON string
    """
    return json.loads(my_str)
