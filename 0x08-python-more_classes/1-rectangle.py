#!/usr/bin/python3
""" this is a module for rectangle objects """


def check_width(width, checkWidthType=isinstance):
    """this func checks width

    1) width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    2) if width is less than 0, raise a ValueError exception with the message width must be >= 0
    
    func returns a tuple (error_code, msg/value) where:
    error_code = 0 if 1 & 2 above are met, value is width
    error_code = 1 if 1 or 2 above is not met, message is "width must be an integer" or "width must be >= 0"
    """

    if (checkWidthType(width, int)) is True:
        if (width >= 0):
            return (0, width)
        else:
            return (1,  'ValueError("width must be >= 0")')
        # endif
    else:
        return (1,  'TypeError("width must be an integer")')
    # endif
# enddef: check_width

def check_height(height, checkHeightType=isinstance):
    """this func checks height

    1) height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    2) if height is less than 0, raise a ValueError exception with the message height must be >= 0
    
    func returns a tuple (error_code, msg/value) where:
    error_code = 0 if 1 & 2 above are met, value is height
    error_code = 1 if 1 or 2  above is not met, message is "height must be an integer" or  "height must be >= 0"
    """

    if (checkHeightType(height, int)) is True:
        if (height >= 0):
            return (0, height)
        else:
            return (1,  'ValueError("height must be >= 0")')
        # endif
    else:
        return (1,  'TypeError("height must be an integer")')
    # endif
# enddef: check_height


class Rectangle():
    """ this creates an empty Rectangle object """
    
    def w_check(self,w, f=check_width):
        """ checks and assigns width variable """
        if (f(w)[0] == 0):
            self._width = f(w)[1]
        else:
            raise eval(f(w)[1])
        # endif
    # enddef: w_check
    
    def h_check(self, h, f=check_height):
        """checks and assigns height variable"""
        if (f(h)[0] == 0):
            self._height = f(h)[1]
        else:
            raise eval(f(h)[1])
        # endif
    # enddef: h_check

    def __init__(self, width=0, height=0):
        """ class constructor """
        self.w_check(width)
        self.h_check(height)
    # enddef: __init__

    @property
    def width(self):
        """getter method for width"""
        return _width
    # enddef: width

    @width.setter
    def width(self, value):
        """setter method for width"""
        self.w_check(value)
    # enddef: width

    @property
    def height(self):
        """getter method for height"""
        return _height
    # enddef: height

    @height.setter
    def height(self, value):
        """setter method for height"""
        self.h_check(value)
    # enddef: height
# endclass:Rectangle
