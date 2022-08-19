#!/usr/bin/python3

def best_score(a_dictionary):
    max_key = None
    max_score = 0
    key_list = []
    idx = 0
    #  ###
    if (a_dictionary is None):
        return None
    else:
        key_list = list(a_dictionary)
    #  endif
    while (idx < len(key_list)):
        if (a_dictionary[key_list[idx]] > max_score):
            max_score = a_dictionary[key_list[idx]]
            max_key = key_list[idx]
        #  endif
        idx = idx + 1
    #  endwhile
    del max_score
    del idx
    del key_list
    return max_key
