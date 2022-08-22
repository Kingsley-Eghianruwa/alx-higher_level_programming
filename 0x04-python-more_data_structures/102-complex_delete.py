#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary)
    idx = 0
    #  ###
    while (idx < len(key_list)):
        if (value == a_dictionary[key_list[idx]]):
            del a_dictionary[key_list[idx]]
        #  endif
        idx = idx + 1
    #  endwhile
    return a_dictionary
#  enddef: complex_delete
