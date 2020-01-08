#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    s = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except IndexError:
            raise IndexError("list out of range")
        except:
            continue
    print("")
    return n
