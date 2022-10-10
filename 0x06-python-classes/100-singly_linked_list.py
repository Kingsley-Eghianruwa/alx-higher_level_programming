#!/usr/bin/python3
"""this is a module for creating  singly linked list"""


def data_check(data):  # ---
    """this function checks that data is an int

    error[0]-> 0 if int, 1 otherwise
    error[1]-> error message if [0] = 1
    """
    error = [None, None]
    if (isinstance(data, int)):
        error[0] = 0
    else:
        error[0] = 1
        error[1] = "TypeError('data must be an integer')"
    #  endif
    return error
#  enddef: data_check ...


def node_check(node):  # ---
    """this function checks if node in an instance of the node class

    error[0]-> 0 if node is of class Node or 1 otherwise
    error[1]-> error message if [0] = 1
    """
    error = [None, None]
    if (isinstance(node, Node) or node is None):
        error[0] = 0
    else:
        error[0] = 1
        error[1] = "TypeError('next_node must be a Node object')"
    #  endif
    return error
#  enddef: node_check ...


class Node:  # ---
    """this creates a node object"""
    def __init__(self, data, next_node=None):
        """node constuctor"""
        d = data_check(data)
        if (d[0] == 0):
            self._data = data
        else:
            raise eval(d[1])
        #  endif
        n_n = node_check(next_node)
        if (n_n[0] == 0):
            self._next_node = next_node
        else:
            raise eval(n_n[1])
        #  endif
        del d
        del n_n
    #  enddef: __init__

    @property
    def data(self):
        """getter function: _data"""
        return self._data
    #  enddef: data

    @data.setter
    def data(self, value):
        """setter function: _data """
        d = data_check(value)
        if (d[0] == 0):
            self._data = value
        else:
            raise eval(d[1])
        #  endif
        del d
    #  enddef: data

    @property
    def next_node(self):
        """getter function: _next_node"""
        return self._next_node
    #  enddef: next_node

    @next_node.setter
    def next_node(self, value):
        nn = node_check(value)
        if (nn[0] == 0):
            self._next_node = value
        else:
            raise eval(nn[1])
        #  endif
        del nn
    #  enddef: next_node
#  endclass: Node ...


class SinglyLinkedList:  # ---
    """this class creates a singly linked list"""

    def __init__(self):
        """class constructor"""
        self._head = None
    #  enddef: __init__

    def sorted_insert(self, value):
        """ creates and inserts a node """
        newNode = Node(value)
        if (self._head is None):
            self._head = newNode
            return None
        else:
            newNode._next_node = self._head
            self._head = newNode
        #  endif
        currentNode = self._head
        status = True
        nodeDataList = []
        while (status is True):
            nodeDataList.append(currentNode._data)
            if (currentNode._next_node is None):
                status = False
            else:
                currentNode = currentNode._next_node
            #  endif
        #  endwhile
        del status
        del currentNode
        currentNode = self._head
        nodeDataList = sorted(nodeDataList)
        n = 0
        while (n < len(nodeDataList)):
            currentNode._data = nodeDataList[n]
            currentNode = currentNode._next_node
            n = n + 1
        #  endwhile
        del n
        del currentNode
        del nodeDataList
    #  enddef: sorted_insert

    def __str__(self):
        aNode = self._head
        status = True
        sdl = []  # SinglyLinkedList data list
        while (status is True and aNode is not None):
            sdl.append("{}".format(aNode._data))
            if (aNode._next_node is not None):
                aNode = aNode._next_node
            else:
                status = False
            #  endif
        #  endwhile
        return '\n'.join(sdl)
    #  enddef: __str__
#  endclass: SinglyLinkedList ...
