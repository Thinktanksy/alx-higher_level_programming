#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    chars_written = 0
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
            chars_written = len(text)
    except OSError:
        pass
    return chars_written
