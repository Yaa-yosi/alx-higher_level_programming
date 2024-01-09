#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename is the name of the file to write into.
        text is the new content to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as new:
        return new.write(text)
