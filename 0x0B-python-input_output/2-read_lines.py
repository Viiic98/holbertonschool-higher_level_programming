#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    i = 0
    with open(filename) as f:
        for line in f:
            i += 1
        if nb_lines <= 0 or nb_lines >= i:
            with open(filename) as f:
                for line in f:
                    print(line, end="")
        else:
            with open(filename) as f:
                for line in f:
                    print(line, end="")
                    nb_lines -= 1
                    if nb_lines == 0:
                        return
