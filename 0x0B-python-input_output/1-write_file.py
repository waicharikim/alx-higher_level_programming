#!/usr/bin/python3
"""
write_file function definition
"""


def write_file(filename="", text=""):
    """
    function writes a string to a text file and returns
    the number of characters written
    """

    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
