#!/usr/bin/python3

# begin_def
def pow(a, b):
    # begin_if
    if (b == 0):
        return 1
    elif (b < 0):
        r = 1.0 / (a ** abs(b))
        return r
    else:
        r = a ** b
        return r
    # end_if
# end_def
