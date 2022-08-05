#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    op_a = []
    op_b = []
    add_a_b = []
    tuple_a_length = len(tuple_a)
    tuple_b_length = len(tuple_b)
    #  ###
    if (tuple_a_length >= 2):
        op_a.append(tuple_a[0])
        op_a.append(tuple_a[1])
    elif (tuple_a_length == 1):
        op_a.append(tuple_a[0])
        op_a.append(0)
    else:
        op_a.append(0)
        op_a.append(0)
    #  endif
    #  ###
    if (tuple_b_length >= 2):
        op_b.append(tuple_b[0])
        op_b.append(tuple_b[1])
    elif (tuple_b_length == 1):
        op_b.append(tuple_b[0])
        op_b.append(0)
    else:
        op_b.append(0)
        op_b.append(0)
    #  endif
    #  ###
    add_a_b.append(op_a[0] + op_b[0])
    add_a_b.append(op_a[1] + op_b[1])
    return tuple(add_a_b)
