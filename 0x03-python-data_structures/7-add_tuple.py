#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        cp_a = tuple_a
    elif len(tuple_a) == 1:
        cp_a = tuple_a[0], 0
    else:
        cp_a = 0, 0
    if len(tuple_b) >= 2:
        cp_b = tuple_b
    elif len(tuple_b) == 1:
        cp_b = tuple_a[0], 0
    else:
        cp_b = 0, 0

    tup = cp_a[0] + cp_b[0], cp_a[1] + cp_b[1]
    return tup
