#!/usr/bin/python3
"""MINIMUM OPERATIONS"""


def minOperations(n: int) -> int:
    """Returns the minimum number of operations needed,
    to result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(int(n / i))
    return n
