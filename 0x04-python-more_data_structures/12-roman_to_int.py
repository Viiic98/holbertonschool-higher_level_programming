#!/usr/bin/python3
def roman_to_int(roman_string):
    n, l, m = 0, len(roman_string), 0

    if roman_string:
        for i in range(l):
            if roman_string[i] == 'I':
                if m == 3:
                    return 0
                if i + 1 < l:
                    if roman_string[i + 1] != 'I':
                        n -= 1
                        m = 0
                    else:
                        n += 1
                        m += 1
                else:
                    n += 1
            elif roman_string[i] == 'V':
                if i + 1 < l:
                    if roman_string[i + 1] != 'V':
                        n += 5
                    else:
                        return 0
                else:
                    n += 5
            elif roman_string[i] == 'X':
                if m == 3:
                    return 0
                if i + 1 < l:
                    if roman_string[i + 1] == 'L':
                        n -= 10
                        m = 0
                    elif roman_string[i + 1] == 'C':
                        n -= 10
                        m = 0
                    elif roman_string[i + 1] != 'X':
                        n += 10
                        m = 0
                    else:
                        n += 10
                        m += 1
                else:
                    n += 10
            elif roman_string[i] == 'L':
                if i + 1 < l:
                    if roman_string[i + 1] != 'l':
                        n += 50
                    else:
                        return 0
                else:
                    n += 50
            elif roman_string[i] == 'C':
                if m == 3:
                    return 0
                if i + 1 < l:
                    if roman_string[i + 1] == 'D':
                        n -= 100
                        m = 0
                    elif roman_string[i + 1] == 'M':
                        n -= 100
                        m = 0
                    else:
                        n += 100
                        m += 1
                else:
                    n += 100
            elif roman_string[i] == 'D':
                n += 500
            elif roman_string[i] == 'M':
                n += 1000
    return n
