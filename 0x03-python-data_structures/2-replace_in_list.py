#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    max_idx = len(my_list) - 1

    if (idx > max_idx or idx < 0):
        return my_list
    else:
        my_list[idx] = element
        return my_list
#  enddef
