#!/usr/bin/python3
"""
class_to_json definition
"""


def class_to_json(obj):

    """
    function returns dictionary description with simple
    data structure for object JSON serialization
    """
    return obj.__dict__
