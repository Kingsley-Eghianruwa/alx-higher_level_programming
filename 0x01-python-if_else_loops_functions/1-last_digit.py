#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = 0
# beginif
if (number >= 0):
    l_digit = number % 10
else:
    l_digit = number % -10
# endif
str = "Last digit of "
# beginif
if (l_digit > 5):
    print(str + "{} is {} and is greater than 5".format(number, l_digit))
elif (l_digit == 0):
    print(str + "{} is {} and is 0".format(number, l_digit))
elif (l_digit < 6 and l_digit != 0):
    l_d = l_digit  # done to make line 18 less tha 80 characters
    print(str + "{} is {} and is less than 6 and not 0".format(number, l_d))
# endif
