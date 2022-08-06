#!/usr/bin/python3

def multiple_returns(sentence):
    str_length = len(sentence)
    str_char = sentence[0]
    if (str_length == 0):
        output = (str_length, None)
    else:
        output = (str_length, str_char)
    #  endif
    return output
