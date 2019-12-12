#!/usr/bin/python3
sys = __import__("sys")

args = sys.argv
len = len(args)

if len == 1:
    print("{:d} arguments.".format(len - 1))
elif len == 2:
    print("{:d} argument:".format(len - 1))
else:
    print("{:d} arguments:".format(len - 1))
for i in range(1, len):
    print("{:d}: {:s}".format(i, args[i]))
