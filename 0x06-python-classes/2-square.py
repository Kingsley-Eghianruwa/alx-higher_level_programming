#!/usr/bin/python3
""" this is a python class module for Square """


def size_check(size):
    """ this function checks that size is an int and >= 0

    status_type(true/false): holds flag for if size is an intger or not
    error(0/1/2): holds error flag,
        error = 0; if size is int and >=0,
        error = 1; if size not int,
        error = 2; if size < 0
    """
    status_type = isinstance(size, int)
    error = None
    if (status_type is True):
        if (size >= 0):
            error = 0
        else:
            error = 2
        #  endif
    else:
        error = 1
    #  endif
    return error


class Square:
    """ this is class creates a square object with size """

    def __init__(self, size=0):
        """class square consructor

        size is a private variable
        size check is done by the size_check() function
        """
        error = size_check(size)
        if (error == 0):
            self.__size = size
        #  endif
        if (error == 1):
            raise TypeError('size must be an integer')
        #  endif
        if (error == 2):
            raise ValueError('size must be >= 0')
        #  endif
        del error
    # enddef: __init__
# endClass: Square
