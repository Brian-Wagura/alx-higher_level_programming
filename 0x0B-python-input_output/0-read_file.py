#!/usr/bin/python3
"""
Reads a file
"""


def read_file(filename=""):
    """ Reads a text file """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')

    except FilenotFoundError:
        pass
