#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys_list = sorted(a_dictionary)
    idx = 0
    #  ###
    while (idx < len(keys_list)):
        print("{}: {}".format(keys_list[idx], a_dictionary[keys_list[idx]]))
        idx = idx + 1
    #  endwhile
