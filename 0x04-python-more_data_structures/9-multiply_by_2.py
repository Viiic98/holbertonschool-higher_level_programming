#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for i in a_dictionary:
        n = new.get(i) * 2
        up = {i: n}
        new.update(up)
    return new
