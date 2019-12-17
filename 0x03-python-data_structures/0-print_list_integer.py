#!/usr/bin/python3
def print_list_integer(my_list=[]):
    l = len(my_list)
    for i in range(l):
        print("{:d}".format(my_list[i]))
