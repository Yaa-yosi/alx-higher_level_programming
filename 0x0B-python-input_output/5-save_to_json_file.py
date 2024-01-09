#!/usr/bin/python3
""""function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as new:
        json.dump(my_obj, new)
