#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    _sum = 0
    for i in range(1, len(argv)):
        _sum += int(argv[i])
    print(_sum)
