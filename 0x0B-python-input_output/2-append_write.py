#!/usr/bin/python3
"""
Appends a string at the end of a textfile(UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Append a string to a text file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
