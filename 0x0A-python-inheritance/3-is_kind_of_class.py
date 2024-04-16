#!/usr/bin/python3
"""
is_kind_of_class function definition
"""


def is_kind_of_class(obj, a_class):
    """ function returns True: object is an instance of,
    or if the object is a class instance inherited from,
    the specified class.
    else: False
    """

    return isinstance(obj, a_class)
