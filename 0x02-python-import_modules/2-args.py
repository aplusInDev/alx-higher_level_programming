#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    size = len(argv)

    if size > 1:
        print("{} arguments: ".format(size - 1))
        for i in range(1, size):
            print("{}: {}".format(i, arg[i]))
    elif size - 1 == 0:
        print("{} arguments.".format(size - 1))
    else:
        print("{} argument:".format(size - 1))
        print("{}: {}".format(size - 1, arg[1]))
