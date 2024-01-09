#!/usr/bin/python3
"""function that appends a string to the end of a text file"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)

    Args:
        filename is the name of the file to write into.
        text is the new content to write to the file.
    """
    with open(filename, "a", encoding="utf-8") as new:
        return new.write(text)
