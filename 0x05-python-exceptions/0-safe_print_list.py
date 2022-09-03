#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0
    count = 0
    while (idx < x):
        try:
            print("{}".format(my_list[idx]), end="")
            count = count + 1
            idx = idx + 1
        except IndexError:
            break
    # endwhile
    print("\n", end="")
    return count
#  enddef: safe_print_list
