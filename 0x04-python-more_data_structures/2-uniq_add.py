#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        c = my_list.count(i)
        if c == 1:
            sum += i
    return sum
