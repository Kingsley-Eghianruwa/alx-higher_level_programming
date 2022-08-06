#!/usr/bin/python3

def multiple_returns(sentence):
    str_length = len(sentence)
    if (str_length == 0):
        str_char = None
    else:
        str_char = sentence[0]
    #  endif
    output = (str_length, str_char)
    return output
