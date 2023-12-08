#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, member in enumerate(new_list):
        if member == search:
            new_list[idx] = replace
    return new_list
