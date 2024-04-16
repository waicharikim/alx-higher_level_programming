#!/usr/bin/python3
"""
inherits from function definition
"""


def inherits_from(obj, a_class):

    """
    function returns True: object is class instance that
    inheriteed from specified class(directly or indirectly)
    else: False
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
