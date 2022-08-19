#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    check = key in a_dictionary
    if (check is True):
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
    #  endif
#  enddef: simple_delete
