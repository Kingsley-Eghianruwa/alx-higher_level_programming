#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    check = key in a_dictionary
    if (check is True):
        del a_dictionary[key]
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    #  endif
    return a_dictionary
#  enddef: update_dictionary
