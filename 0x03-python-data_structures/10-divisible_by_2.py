#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    idx = 0
    max_idx = len(my_list) - 1
    #  ###
    while (idx <= max_idx):
        mod = my_list[idx] % 2
        if (my_list[idx] == 1 or my_list[idx] == 0 or my_list[idx] == -1):
            new_list.insert(idx, False)
        elif (mod == 0):
            new_list.insert(idx, True)
        else:
            new_list.insert(idx, False)
        #  endif
        idx = idx + 1
    #  endwhile
    return new_list
