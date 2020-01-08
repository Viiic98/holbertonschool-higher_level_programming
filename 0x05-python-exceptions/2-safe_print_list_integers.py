def safe_print_list_integers(my_list=[], x=0):
    n = 0
    s = 0
    for i in range(x):
        if x == 0:
            break
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            raise IndexError("list out of range")
        except:
            continue
        n += 1
        x -= 1
    if n > 0:
        print("")
    return n
