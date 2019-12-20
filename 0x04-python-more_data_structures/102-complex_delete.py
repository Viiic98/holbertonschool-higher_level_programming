#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        ls = []
        for i in a_dictionary:
            if a_dictionary.get(i) == value:
                ls.append(i)
        for i in ls:
            a_dictionary.pop(i)
        else:
            return None
    else:
        return None
