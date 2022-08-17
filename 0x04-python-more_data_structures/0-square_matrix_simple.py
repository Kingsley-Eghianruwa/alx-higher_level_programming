#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    idx_i = 0
    idx_j = 0
    len_row = len(matrix)
    len_col = len(matrix[0])
    new_matrix = []
    #  ####
    while (idx_i < len_row):
        new_matrix.append([])
        while (idx_j < len_col):
            new_matrix[idx_i].append((matrix[idx_i][idx_j])**2)
            idx_j = idx_j + 1
        #  endwhile
        idx_j = 0
        idx_i = idx_i + 1
    #  endwhile
    return new_matrix
#  enddef: square_matrix_simple
