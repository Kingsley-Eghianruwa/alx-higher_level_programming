#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    idx = 0
    len_list = len(my_list)
    #  ###
    while (idx < len_list):
        if (my_list[idx] == search):
            new_list.append(replace)
        else:
            new_list.append(my_list[idx])
        #  endif
        idx = idx + 1
    #  endwhile
    return new_list
#  enddef: search_replace
