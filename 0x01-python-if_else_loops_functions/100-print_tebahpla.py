#!/usr/bin/python3

char_start = 122
char_case = -1
# begin_for
for i in range(1, 27):
    # begin_if
    if (char_case == -1):
        print("{}".format(chr(char_start)), end="")
    else:
        print("{}".format(chr(char_start - 32)), end="")
    # end_if
    char_start = char_start - 1
    char_case = char_case * -1
# end_for

    

        

        
