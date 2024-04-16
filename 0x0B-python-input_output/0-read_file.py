#!/usr/bin/python3
"""
read_file function definition
"""


def read_file(filename=""):
    """
    function reads a file and prints to stdout
    """
    f = open(filename, 'r', encoding="UTF8")
    with open(filename) as f:
        for line in f:
            print(line, end='')
