#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    size = len(argv) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, argv[i]))
    elif size == 0:
        print("{} arguments.".format(size))
    else:
        print("{} argument:".format(size))
        print("{}: {}".format(size, argv[1]))
