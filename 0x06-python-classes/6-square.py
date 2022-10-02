#!/usr/bin/python3
""" this is a python class module for Square """


def size_check(size):
    """ this function checks that size is an int and >= 0

    status_type(true/false): holds flag for if size is an intger or not
    error[0]=(0/1/2): holds error flag,
        error = 0; if size is int and >=0,
        error = 1; if size not int,
        error = 2; if size < 0
    error[1] hold the exception to be raised
    """
    status_type = isinstance(size, int)
    error = [None, None]
    if (status_type is True):
        if (size >= 0):
            error[0] = 0
        else:
            error[0] = 2
            error[1] = "ValueError('size must be >= 0')"
        #  endif
    else:
        error[0] = 1
        error[1] = "TypeError('size must be an integer')"
    #  endif
    return tuple(error)
#  enddef: size_check


def position_check(position):
    """This function checks position is a tuple of 2 positive integers

    error[0]=(0/1) flag for position if a tuple of positive int(0) or not(1)
    error[1]= exception to be raised if error[0] != 0
    """
    error = [None, None]
    test = [True, True, True]
    test_pos = [None, None, None]
    if (len(position) == 2):
        test_pos[0] = isinstance(position[0], int) and position[0] >= 0
        test_pos[1] = isinstance(position[1], int) and position[1] >= 0
        test_pos[2] = len(position) == 2
    #  endif
    if (test_pos == test):
        error[0] = 0
    else:
        error[0] = 1
        m = "TypeError('position must be a tuple of 2 positive integers')"
        error[1] = m
    #  endif
    return tuple(error)
#  enddef: position_check


def linePrinter(char, noOfTimes):
    """this print a char n times"""
    n = 0
    while (n < noOfTimes):
        print(char, end="")
        n = n + 1
    #  endwhile
#  enddef: linePrinter


class Square:
    """ this is class creates a square object with size """

    def __init__(self, size=0, position=(0, 0)):
        """class square consructor

        size is a private variable
        size check is done by the size_check() function
        """
        errorSize = size_check(size)
        if (errorSize[0] == 0):
            self._size = size
        else:
            raise eval(errorSize[1])
        #  endif
        errorPos = position_check(position)
        if (errorPos[0] == 0):
            self._position = position
        else:
            raise eval(errorPos[1])
        #  endif
        del errorPos
        del errorSize
    # enddef: __init__

    def area(self):
        """ this method caluculates the square area """
        a = pow(self._size, 2)
        return a
    #  enddef: area

    @property
    def size(self):
        """getter for the size private attribute"""
        return self._size
    #  enddef: size

    @size.setter
    def size(self, value):
        """setter for size private attribute"""
        e = size_check(value)
        if (e[0] == 0):
            self._size = value
        else:
            raise eval(e[1])
        #  endif
    #  enddef: size

    @property
    def position(self):
        """getter for the position private attribute"""
        return self._position
    #  enddef: position

    @position.setter
    def position(self, value):
        """setter for the position private attribute"""
        e = position_check(value)
        if (e[0] == 0):
            self._position = value
        else:
            raise eval(e[1])
        #  endif
    # enddef: position

    def my_print(self):
        """prints in stdout the square with the character #"""
        i = 0
        j = 0
        max_iter = None
        if (self._size > 0):
            max_iter = self._size - 1
        else:
            max_iter = 0
        #  endif
        while (i <= max_iter):
            if (max_iter != 0):
                linePrinter(" ", self._position[0])
                linePrinter("#", self._size)
            #  endif
            print("\n", end="")
            i = i + 1
        #  endwhile
    #  enddef: my_print
# endClass: Square
