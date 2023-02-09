#!/usr/bin/python3
def min_operations(n):
    operations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            operations += 1
        else:
            n = n - 1
            operations += 1
    return operations
