#!/usr/bin/python3
"""function that defines a class_to_json"""


def class_to_json(obj):
    """Return the dictionary description a simple data structure."""
    return obj.__dict__
