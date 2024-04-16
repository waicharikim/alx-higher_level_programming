#!/usr/bin/python3
"""
append_after function definition
"""


def append_after(filename="", search_string="", new_string=""):

    """
    inserts a text line to a file, after each line
    containing a specific string
    """

    text = ''
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as i:
        i.write(text)
