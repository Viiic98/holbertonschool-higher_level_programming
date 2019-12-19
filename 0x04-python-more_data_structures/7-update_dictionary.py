#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    up = {key: value}
    a_dictionary.update(up)
    new = a_dictionary
    return new
