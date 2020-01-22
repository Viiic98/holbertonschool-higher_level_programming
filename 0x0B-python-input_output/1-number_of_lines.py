#!/usr/bin/python3
def number_of_lines(filename=""):
    i = 0
    with open(filename) as f:
        for line in f:
            i += 1
        return i
