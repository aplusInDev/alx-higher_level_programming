#!/usr/bin/python3
"""
This Module for the function pascal_triangle()
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n (int)
    """
    if n <= 0:
        return []
    t1 = [[1]]
    for i in range(n - 1):
        result = []
        for j in range(i + 2):
            if j == 0:
                x = 0
                y = t1[i][j]
            elif j == i + 1:
                x = t1[i][j - 1]
                y = 0
            else:
                x = t1[i][j - 1]
                y = t1[i][j]
            result.append(x + y)
        t1.append(result)
    return t1
