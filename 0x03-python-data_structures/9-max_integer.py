#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        big = my_list[0]
        for i in my_list:
            if i > big:
                big = i
        return big
    else:
        return None
