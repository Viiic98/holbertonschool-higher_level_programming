#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0

    for i in range(len(roman_string)):
        non = 0
        l = roman_string[i]
        if roman_string.count(l) > 3:
            return 0
        for j in rom_d:
            if l == j:
                non += 1
                break
        if non == 0:
            return 0
        if len(roman_string) - 1 > i:
            ln = roman_string[i + 1]
            if rom_d.get(l) < rom_d.get(ln):
                sum -= rom_d.get(l)
            else:
                sum += rom_d.get(l)
        else:
            sum += rom_d.get(l)

    return sum
