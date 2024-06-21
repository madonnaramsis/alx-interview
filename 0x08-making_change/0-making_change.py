#!/usr/bin/python3
"""
This module contains a function to calculate the fewest number of coins
needed to meet a given total amount.

The makeChange function takes in two parameters:
- coins: A list of coin values available.
- total: The target amount.

It returns the fewest number of coins needed to reach the total,
or -1 if it is not possible.
"""


def makeChange(coins, total):
    """
    Calculate the fewest number needed to meet a given total amount.

    Args:
        coins (list): A list of coin values available.
        total (number): The target amount.

    Returns:
        int: The fewest number of coins needed to reach the total,
        or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, ncoins = (0, 0)
    cpy_total = total
    len_coins = len(coins)

    while (i < len_coins and cpy_total > 0):
        if (cpy_total - coins[i]) >= 0:
            cpy_total -= coins[i]
            ncoins += 1
        else:
            i += 1

    check = cpy_total > 0 and ncoins > 0
    return -1 if check or ncoins == 0 else ncoins
