#!/usr/bin/python

import sys

cache = {}


def making_change(amount, denominations):
    # base case
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif amount in cache:
        return cache[amount]
    else:
        x = (
            making_change(amount - 1)
            + making_change(amount - 5)
            + making_change(amount - 10)
            + making_change(amount - 25)
            + making_change(amount - 50)
        )
        cache[amount] = x
        return x


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")
