#!/usr/bin/python3

# begin_for
for i in range(0, 10):
    # begin_for
    for j in range(0, 10):
        # begin_if
        if (i != j and i < j):
            print("{}{}".format(i, j), end="")
            # begin_if
            if (i == 8 and j == 9):
                print('\n', end="")
            else:
                print(", ", end="")
            # end_if
        # end if
    # end_for
# end_for
