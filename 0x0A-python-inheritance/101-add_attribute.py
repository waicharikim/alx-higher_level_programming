#!/usr/bin/python3
"""
add new_attribute function definition
"""


def add_attribute(obj, attr, value):
    """
    function adds new attribute to an object
    hasattr - has attribute
    setattr - set attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
