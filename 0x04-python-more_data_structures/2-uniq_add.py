#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    uniq_list = list(set(my_list))
    result = sum(uniq_list)
    return result
