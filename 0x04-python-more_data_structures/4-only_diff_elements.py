#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for i in set_1:
        f = 0
        for j in set_2:
            if j == i:
                f = 1
                break
        if f == 0:
            new.append(i)
    for i in set_2:
        f = 0
        for j in set_1:
            if j == i:
                f = 1
                break
        if f == 0:
            new.append(i)
    return new
