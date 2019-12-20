#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        ls = []
        for i in a_dictionary:
            if a_dictionary.get(i) == value:
                ls.append(i)
        for i in ls:
            a_dictionary.pop(i)
        return a_dictionary
    else:
        return None
