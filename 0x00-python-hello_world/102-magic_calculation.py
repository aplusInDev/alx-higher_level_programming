#!/usr/bin/python3
def magic_calculation(a, b):
        return a + b - ((a & 0xFFFF) + (b & 0xFFFF))
