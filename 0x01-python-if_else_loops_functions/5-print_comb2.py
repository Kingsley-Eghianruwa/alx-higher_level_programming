#!/usr/bin/python3

# begin_for
for i in range(0, 100):
    # begin_if
    if (i == 99):
        print("{:02}".format(i))
    else:
        print("{:02}, ".format(i), end="")
    # end_if
# end_for
