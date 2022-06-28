#!/usr/bin/python3

# begin_def
def fizzbuzz():
    # begin_for
    for i in range(1, 101):
        # begin_if
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz ", end="")
        elif (i % 3 == 0 and i % 5 != 0):
            print("Fizz ", end="")
        elif (i % 3 != 0 and i % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
    # end_for
# end_def
