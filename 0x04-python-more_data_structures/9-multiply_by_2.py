#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = a_dictionary.copy()
    for key, val in a_dict.items():
        a_dict[key] = val * 2
    return a_dict
