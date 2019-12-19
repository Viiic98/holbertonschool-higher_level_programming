#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        c = my_list.count(i)
        while c > 1:
            my_list.remove(i)
            c = my_list.count(i)
    for i in my_list:
        sum += i
    return sum
