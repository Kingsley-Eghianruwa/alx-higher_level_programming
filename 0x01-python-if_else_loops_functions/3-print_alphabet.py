#!/usr/bin/python3

# begin_for
for i in range(97, 123):
    # begin_if
    if (chr(i) == 'e' or chr(i) == 'q'):
        continue
    else:
        print("{}".format(chr(i)), end="")
    #end_if
# end_for
