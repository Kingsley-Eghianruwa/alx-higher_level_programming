#!/usr/bin/pydoc3

def print_list_integer(my_list=[]):
    l_max_idx = len(my_list) - 1
    index = 0
    while (index <= l_max_idx):
        print("{}".format(my_list[index]))
        index = index + 1
    #  endwhile
#  enddef
