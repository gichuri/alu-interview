#!/usr/bin/python3

""" get rain retained in walls"""


def rain(walls):
    """ function that calculates water retained"""
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


# Example usage
walls = [0, 1, 0, 2, 0, 3, 0, 4]
water_retained = get_water_retained(walls)
print(water_retained)  # Output: 6
