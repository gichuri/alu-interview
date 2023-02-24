#!/usr/bin/python3

"""
calculate the amount of water retained
"""


def rain(walls):
    """
    Calculate the amount of rainwater retained by the given walls.

    Args:
    walls (list of int): A list of non-negative integers representing the heights of walls with unit width 1.

    Returns:
    int: The total amount of water retained in the walls, in square units.

    Example:
    >>> rain([0, 1, 0, 2, 0, 3, 0, 4])
    6

    """

    if len(walls) == 0:
        continue
    else:
        n = len(walls)
        left = [0] * n
        right = [0] * n

        left[0] = walls[0]
        for i in range(1, n):
            left[i] = max(left[i-1], walls[i])

        right[n-1] = walls[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], walls[i])

        water = 0
        for i in range(n):
            water += max(0, min(left[i], right[i]) - walls[i])

        return water
