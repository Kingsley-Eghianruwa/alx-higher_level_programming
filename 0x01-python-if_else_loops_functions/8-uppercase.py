#!/usr/bin/python3


# begin_def
def uppercase(str):
    str = str + '\n'
    index_length = len(str)
    # begin_for
    for index in range(0, index_length):
        var = ord(str[index])
        # begin_if
        if (var >= 97 and var <= 122):
            print("{}".format(chr(var - 32)), end="")
        else:
            print("{}".format(chr(var)), end="")
        # end_if
    # end_for
# end_def
