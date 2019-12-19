#!/usr/bin/python3
def roman_to_int(roman_string):
    n, l = 0, len(roman_string)
    if roman_string:
        for i in range(l):
            if roman_string[i] == 'I':
                if i + 1 < l:
                    if roman_string[i + 1] != 'I':
                        n -= 1
                    else:
                        n += 1
                else:
                    n += 1
            elif roman_string[i] == 'V':
                n += 5
            elif roman_string[i] == 'X':
                if i + 1 < l:
                    if roman_string[i + 1] == 'L':
                        n -= 10
                    elif roman_string[i + 1] == 'C':
                        n -= 10
                    else:
                        n += 10
                else:
                    n += 10
            elif roman_string[i] == 'L':
                n += 50
            elif roman_string[i] == 'C':
                if i + 1 < l:
                    if roman_string[i + 1] == 'D':
                        n -= 100
                    elif roman_string[i + 1] == 'M':
                        n -= 100
                    else:
                        n += 100
                else:
                    n += 100
            elif roman_string[i] == 'D':
                n += 500
            elif roman_string[i] == 'M':
                n += 1000
    return n
