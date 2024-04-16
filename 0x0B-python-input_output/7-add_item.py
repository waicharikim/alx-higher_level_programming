#!/usr/bin/python3
"""
script adds all arguments to a Python list
"""


import sys


if __name__ == '__main__':
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file
    try:
        loaded = load_json('add_item.json')
    except FileNotFoundError:
        loaded = []
    loaded.extend(sys.argv[1:])
    save_json(loaded, 'add_item.json')
