#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    cmdL_arg = sys.argv
    len_vec = len(cmdL_arg) - 1
    index = 0
    if len_vec == 0:
        print("{} arguments.".format(len_vec))
    elif len_vec == 1:
        print("{} argument:".format(len_vec))
        print("{}: {}".format(len_vec, cmdL_arg[1]))
    elif len_vec > 1:
        print("{} arguments:".format(len_vec))
        index = 1
        while index <= len_vec:
            print("{}: {}".format(index, cmdL_arg[index]))
            index = index + 1
        #  endwhile
    # endif
