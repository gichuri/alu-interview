#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that
returns a list of lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for item in range(n-1):
        pascal.append(
            [i+j for i, j in zip([0] + pascal[-1], pascal[-1] + [0])])

    return 
