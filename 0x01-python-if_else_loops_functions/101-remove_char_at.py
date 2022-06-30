#!/usr/bin/python3

# begin_def
def remove_char_at(str, n):
    string_length = len(str)
    str2 = ""
    # begin_if
    if (n > string_length or n < 0):
        return str
    else:
        # begin_for
        for i in range(0, string_length):
            # begin_if
            if (i == n):
                continue
            else:
                str2 = str2 + str[i]
            # end_if
        # end_for
    # end_if
    return str2
# end_def
