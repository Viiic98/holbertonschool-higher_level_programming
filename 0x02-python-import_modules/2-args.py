#!/usr/bin/python3
sys = __import__("sys")

args = sys.argv
len = len(args)

if len == 1:
    print("0 arguments.")
elif len == 2:
    print("1 argument:")
else:
    print("{:d} arguments:".format(len - 1))
for i in range(1, len):
    print("{:d}: {}".format(i, args[i]))
