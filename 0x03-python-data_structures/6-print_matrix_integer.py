#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    max_col = len(matrix[0]) - 1
    max_row = len(matrix) - 1
    if (max_col == -1 and max_row == 0):
        print('')
    else:
        r_idx = 0
        c_idx = 0
        #  ###
        while (r_idx <= max_row):
            while (c_idx <= max_col):
                if (c_idx == max_col):
                    print("{:d}\n".format(matrix[r_idx][c_idx]), end='')
                else:
                    print("{:d}".format(matrix[r_idx][c_idx]), end=' ')
                c_idx = c_idx + 1
                #  endif
            #  endwhile
            c_idx = 0
            r_idx = r_idx + 1
        #  endwhile
    #  endif
