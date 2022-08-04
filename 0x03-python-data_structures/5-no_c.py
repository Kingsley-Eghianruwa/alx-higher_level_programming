#!/usr/bin/python3

def no_c(my_string):
    char_list = []
    max_idx = len(my_string) - 1
    idx = 0

    while (idx <= max_idx):
        if (my_string[idx] != 'c' and  my_string[idx] != 'C'):
            char_list.append(my_string[idx])
        #  endif
        # space
        idx = idx + 1
    #  endwhile

    return(''.join(char_list))
