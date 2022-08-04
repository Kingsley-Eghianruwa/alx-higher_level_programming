#!/usr/bin/python3

def element_at(my_list, idx):
    max_idx = len(my_list) - 1

    if (idx > max_idx or idx < 0):
        return None
    else:
        return(my_list[idx])
#  enddef
