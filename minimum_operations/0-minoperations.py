#!/usr/bin/python3

""" find the minimum no of ops req"""


def minOperations(n):

    """  calculates the fewest number of operations needed"""

    operations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            operations += 1
        else:
            n = n - 1
            operations += 1
    return operations
