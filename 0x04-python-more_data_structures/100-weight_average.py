#!/usr/bin/python3

def weight_average(my_list=[]):
    top = 0
    bottom = 0
    idx = 0
    result = 0
    #  ###
    if (my_list == []):
        return 0
    else:
        max_idx = len(my_list) - 1
    #  endif
    #  ###
    while (idx <= max_idx):
        tmp = list(my_list[idx])
        top = top + (tmp[0] * tmp[1])
        bottom = bottom + tmp[1]
        idx = idx + 1
    #  endwhile
    result = (top * 1.00) / (bottom * 1.00)
    return result
#  enddef: weight_average
