#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    key_list = list(a_dictionary)
    new_list = []
    idx = 0
    #  ###
    while (idx < len(key_list)):
        k = key_list[idx]
        v = a_dictionary[k] * 2
        new_list.append((k, v))
        idx = idx + 1
    #  endwhile
    del idx
    new_dict = dict(new_list)
    return new_dict
