#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    len = len(args)
    sum = 0

    for i in range(1, len):
        sum += int(args[i])
    print("{:d}".format(sum))
