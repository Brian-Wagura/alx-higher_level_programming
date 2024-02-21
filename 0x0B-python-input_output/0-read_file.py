#!/usr/bin/python3
"""
Reads a file
"""


def read_file(filename=""):
    """ Reads a text file """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read(), end='')
    except FilenotFoundError:
        pass
