#!/usr/bin/python3
var = 0
for a in range(122, 96, -1):
    if var > 0:
        var = 0
    print("{}".format(chr(a + var)), end='')
    if var == 0:
        var = 32
    var *= -1
