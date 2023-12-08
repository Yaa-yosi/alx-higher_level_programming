#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_member = set_1.intersection(set_2)
    for member in common_member:
        return member
