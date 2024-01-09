#!/usr/bin/python3
#"""Function to read a file."""

#def read_file(filename=""):
#    """Reads a text file UTF8 and prints it to stdout."""
#    with open(filename, encoding="utf-8") as new:
#        print(new.read(), end="")
#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
