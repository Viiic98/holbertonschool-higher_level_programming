#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for i in range(x):
        if x == 0:
            break
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        n += 1
        x -= 1
    if n > 0:
        print("")
    return n
