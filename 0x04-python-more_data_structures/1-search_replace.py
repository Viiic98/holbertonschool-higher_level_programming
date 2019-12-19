#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    a = 0
    for i in my_list:
        if i == search:
            new[a] = replace
        else:
            new[a] = i
        a += 1
    return new
