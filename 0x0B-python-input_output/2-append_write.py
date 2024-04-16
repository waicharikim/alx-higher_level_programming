#!/usr/bin/python3
"""
append_write function description
"""


def append_write(filename="", text=""):
    """
    function appends a string at the end of a text file
    and returns the added characters number
    """

    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
