#!/usr/bin/python3
"""script to solve the coins-change problem"""


def makeChange(coins, total):
    """func def"""
    if total <= 0:
        return 0

    table = [total + 1] * (total + 1)

    table[0] = 0
    for i in range(1, len(table)):
        for coin in coins:
            if i >= coin:
                table[i] = min(table[i], table[i - coin] + 1)

    if table[total] != total + 1:
        return table[total]
    else:
        return -1
