#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        for key1 in a_dictionary:
            if key1 == key:
                a_dictionary[key] = value
                return a_dictionary
            elif key1 != key:
                a_dictionary[key] = value
                return a_dictionary

