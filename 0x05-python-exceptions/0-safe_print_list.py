#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x == 0 or len(my_list) == 0:
            return 0
        n = 0
        for i in my_list:
            if x == 0:
                return n
            print(i, end="")
            n += 1
            x -= 1
        print("")
        return n
    except:
        print("Unexpected error printing the list")
