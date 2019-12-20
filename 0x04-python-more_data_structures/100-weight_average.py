#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    weight = 0
    if my_list:
        for i in my_list:
            k, mul = 0, 0
            for j in i:
                if k == 1:
                    weight += j
                    mul *= j
                    k = 0
                    break
                mul += j
                k += 1
            sum += mul
    else:
        return 0
    return sum / weight
