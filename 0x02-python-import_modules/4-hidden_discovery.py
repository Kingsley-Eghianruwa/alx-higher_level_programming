#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as H4
    var = dir(H4)
    index = 0
    len_var = len(var) - 1

    while (index <= len_var):
        if (var[index][0] != '_' and var[index][1] != '_'):
            print("{}".format(var[index]))
        #  endif
        index = index + 1
    #  endwhile


