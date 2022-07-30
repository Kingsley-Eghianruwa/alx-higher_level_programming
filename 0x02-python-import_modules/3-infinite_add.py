#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0
    index = 1
    arg_vec = sys.argv
    argv_len = len(arg_vec) - 1
    while index <= argv_len:
        sum = sum + int(arg_vec[index])
        index = index + 1
    #  endwhile
    print("{}".format(sum))
