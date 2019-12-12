#!/usr/bin/python3
sys = __import__("sys")

args = sys.argv
len = len(args)
print("{:d} arguments:".format(len - 1))
for i in range(1, len):
    print("{:d}: {}".format(i, args[i]))
