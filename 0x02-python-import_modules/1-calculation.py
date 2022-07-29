#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    tmp = 0

    tmp = cal.add(a, b)
    print("{} + {} = {}".format(a, b, tmp))
    tmp = cal.sub(a, b)
    print("{} - {} = {}".format(a, b, tmp))
    tmp = cal.mul(a, b)
    print("{} * {} = {}".format(a, b, tmp))
    tmp = cal.div(a, b)
    print("{} / {} = {}".format(a, b, tmp))
