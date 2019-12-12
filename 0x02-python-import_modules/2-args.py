#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    len = len(args)

    if len == 1:
        print("{:d} arguments.".format(len - 1))
    else:
        if len == 2:
            print("{:d} argument:".format(len - 1))
        else:
            print("{:d} arguments:".format(len - 1))
        for i in range(1, len):
            print("{:d}: {:s}".format(i, args[i]))
