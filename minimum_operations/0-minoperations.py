#!/usr/bin/python3

""" find the minimum no of ops req"""


def minOperations(n):
    """Create sum"""

    if type(n) is not int or n <= 1:
        return 0
    operations_sum = []
    divisor = 2
    while (n % divisor) is 0 and (n // divisor) is not 1:
        operations_sum.append(divisor)
        n = n // divisor
    divisor = 3
    while n > divisor:
        while (n % divisor) is 0 and (n // divisor) is not 1:
            operations_sum.append(divisor)
            n = n // divisor
        divisor += 2
    operations_sum.append(n)
    return sum(operations_sum)
