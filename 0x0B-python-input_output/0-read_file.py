#!/usr/bin/python3
"""Function to read a file."""

def read_file(filename=""):
    """Reads a text file UTF8 and prints it to stdout."""
    with open(filename, encoding="utf-8") as new:
        print(new.read(), end="")
