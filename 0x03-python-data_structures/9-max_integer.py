#!/usr/bin/python3

def max_integer(my_list=[]):
    list_length = len(my_list)
    max_value = 0
    max_idx = list_length - 1
    idx = 0
    #  ###
    if (list_length == 0):
        return None
    else:
        max_value = my_list[0]
    #  endif
    while (idx <= max_idx):
        if (my_list[idx] > max_value):
            max_value = my_list[idx]
        #  endif
        idx = idx + 1
    #  endwhile
    return max_value
