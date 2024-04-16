#!/usr/bin/python3
"""
is_same_class function definition
"""


def is_same_class(obj, a_class):

    """
    function returns True if object is exactly
    an instance of the specified class;
    else returns False
    """

    return type(obj) == a_class
