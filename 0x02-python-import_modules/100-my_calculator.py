#!/usr/bin/python3

from sys import argv
import calculator_1 as calculator
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    print("{} {} {} =".format(a, op, b), end=' ')
    if op == '+':
        print("{}".format(calculator.add(a, b)))
    elif op == '-':
        print("{}".format(calculator.sub(a, b)))
    elif op == '*':
        print("{}".format(calculator.mul(a, b)))
    else:
        print("{}".format(calculator.div(a, b)))
