#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    arg_vec = sys.argv
    arg_count = len(arg_vec)

    if (arg_count == 4):
        op_a = int(arg_vec[1])
        op_b = int(arg_vec[3])
        op = arg_vec[2]
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    #  endif

    if (op == '+'):
        print("{} {} {} = {}".format(op_a, op, op_b, calc.add(op_a, op_b)))
        sys.exit(0)
    elif (op == '-'):
        print("{} {} {} = {}".format(op_a, op, op_b, calc.sub(op_a, op_b)))
        sys.exit(0)
    elif (op == '*'):
        print("{} {} {} = {}".format(op_a, op, op_b, calc.mul(op_a, op_b)))
        sys.exit(0)
    elif (op == '/'):
        print("{} {} {} = {}".format(op_a, op, op_b, calc.div(op_a, op_b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    #  endif
