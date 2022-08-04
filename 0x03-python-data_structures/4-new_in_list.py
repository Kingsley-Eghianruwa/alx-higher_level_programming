#!/usr/bin/python3

def copy_list(my_list, new_list=[]):
    index = 0

    if (my_list is None):
        new_list = None
        return new_list
    else:
        max_index = len(my_list) - 1
    #  endif

    while (index <= max_index):
        new_list[index] = my_list[index]
        index = index + 1
    #  endwhile

    return new_list
#  enddef:copy_list


def new_in_list(my_list, idx, element):
    new_list = []
    new_list = copy_list(my_list, new_list)

    if (my_list is None):
        return new_list
    else:
        max_idx = len(my_list) - 1
    #  endif

    if ((idx < 0) or (idx > max_index)):
        return new_list
    #  endif

    new_list[idx] = element
    return new_list
#  enddef:new_in_list
