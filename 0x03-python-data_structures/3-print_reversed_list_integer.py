#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if (my_list == None):
        return None
    else:
        max_idx = len(my_list) - 1
    
    index = max_idx

    while (index >= 0):
        print("{:d}".format(my_list[index]))
        index = index - 1
    #  endwhile
#  enddef
