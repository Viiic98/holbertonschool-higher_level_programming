#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0

    if type(roman_string) is not str or (roman_string) is None:
        return 0
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
            if sum != 0 and sum < rom_d.get(ln):
                return 0
            elif l == 'V' and ln == 'V':
                return 0
            elif l == 'L' and ln == 'L':
                return 0
            elif l == 'D' and ln == 'D':
                return 0
            elif rom_d.get(l) < rom_d.get(ln):
                if l == 'I':
                    if ln == 'V' or ln == 'X':
                        sum -= rom_d.get(l)
                    else:
                        return 0
                elif l == 'X':
                    if ln == 'L' or ln == 'C':
                        sum -= rom_d.get(l)
                    else:
                        return 0
                elif l == 'C':
                    if ln == 'D' or ln == 'M':
                        sum -= rom_d.get(l)
                    else:
                        return 0
                else:
                    return 0
            else:
                sum += rom_d.get(l)
        else:
            sum += rom_d.get(l)

    return sum
