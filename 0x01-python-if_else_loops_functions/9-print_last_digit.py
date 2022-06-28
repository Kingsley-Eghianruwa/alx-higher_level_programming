#!/usr/bin/python3

# begin_def
def print_last_digit(number):
    l_digit = 0
    # beginif
    if (number >= 0):
        l_digit = abs(number % 10)
    else:
        l_digit = abs(number % -10)
    # endif
    print("{}".format(l_digit), end="")
    return l_digit
# end_def
