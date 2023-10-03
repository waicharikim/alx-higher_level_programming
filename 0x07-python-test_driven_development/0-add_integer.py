#!/usr/bin/python3
"""Defines a function that adds integers."""


def add_integer(a, b=98):
    """Returns the sum of a and b.

    Float arguments are typecasted to int datatype  before addition.

    Raises:
        TypeError: If either of a or b is a not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
