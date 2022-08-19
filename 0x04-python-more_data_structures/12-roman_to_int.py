#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_symbols = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    idx = len(roman_string) - 1
    cmp_x = 0
    sum_digits = 0
    #  ###
    if (roman_string is None):
        return 0
    #  endif
    if (type(roman_string) is not  str):
        return 0
    #  endif
    while (idx >= 0):
        z = roman_symbols[roman_string[idx]]
        if (z >= cmp_x):
            sum_digits = sum_digits + z
        else:
            sum_digits = sum_digits - z
        #  endif
        cmp_x = z
        idx = idx - 1
    #  endwhile
    return sum_digits
#  enddef: roman_to_int
