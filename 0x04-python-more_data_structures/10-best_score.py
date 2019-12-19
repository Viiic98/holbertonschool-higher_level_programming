#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = a_dictionary.values()
        m = max(val)
        for i in a_dictionary:
            if a_dictionary.get(i) == m:
                return i
    else:
        return None
