"""
We'll say that a positive int divides itself if every digit in the number
divides into the number evenly. So for example 128 divides itself since 1, 2,
and 8 all divide into 128 evenly.

And we'll say that 0 does not divide into anything evenly, so no number with
0 digit divides itself.

Write a function to determine if a number divides itself.
"""

"""
Single integers only, no floats or strings
Numbers can be negative or positive
Input: Single int arg
Return: Boolean, True if divides itself
"""


def divides_self(n):
    # split the original num
    digits = [int(i) for i in str(n)]
    # divide each split by original num
    for d in digits:
        # if 0 exists, answer is False
        # check if division is even -> n % 2 == 0
        if (d == 0) or (n % d != 0):
            return False
    # if we get here, the number is good
    return True


# print(24, divides_self(24))
# print(128, divides_self(128))
# print(108, divides_self(108))

"""
The Knapsack Problem

We have a bunch of objects, We want to maximize the value of our haul.
The knapsack has limited weight capacity.
Items have weights and values.
Which items do we take to maximize value?
"""

"""
General Approaches
* Naive -> whatever you came up with first that works
* Brute Force -> try everything and choose the best one
* Greedy -> make the move that's most to your current advantage

"""

"""
Explorer's Dilemna - aka the Knapsack Problem
After spending several days exploring a deserted island out in the Pacific,
you stumble upon a cave a full of pirate loot! There are coins, jewels,
paintings, and many other types of valuable objects.

However, as you begin to explore the cave and take stock of what you've
found, you hear something. Turning to look, the cave has started to flood!
You'll need to get to higher ground ASAP.

There IS enough time for you to fill your backpack with some of the items
in the cave. Given that...
- you have 60 seconds until the cave is underwater
- your backpack can hold up to 50 pounds
- you want to maximize the value of the items you retrieve (since you can
only make one trip)

HOW DO YOU DECIDE WHICH ITEMS TO TAKE?
"""

import random
import time
from itertools import combinations


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f"{self.name}, {self.weight} lbs, ${self.value}"


small_cave = []
medium_cave = []
large_cave = []


def fill_cave_with_items():
    """Randomly generates Item objects and
    creates caves of different sizes for testing"""

    names = [
        "painting",
        "jewel",
        "coin",
        "statue",
        "treasure chest",
        "gold",
        "silver",
        "sword",
        "goblet",
        "hat",
    ]

    for _ in range(5):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))

    for _ in range(15):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        medium_cave.append(Item(n, w, v))

    for _ in range(25):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        large_cave.append(Item(n, w, v))


def print_results(items, knapsack):
    """Print out the contents of what the algorithm
    calculated should be added to the knapsack"""

    # print (f'\nItems in the cave:')
    # for i in items:
    #     print (i)

    total = 0

    print("\nBest items to put in knapsack:\n")
    for item in knapsack:
        print(f"* {item}")
        total += item.value
    print(f"\nTotal value: ${total}")
    print(f"\nResult calculated in {time.time()-start:.5f} seconds")
    print("--------------------------------------")


def naive_fill_knapsack(sack, items):
    """#Put highest value items in knapsack until full
    (other basic, naive approaches exist)"""

    # sort items by value
    items.sort(key=lambda el: el.value, reverse=True)

    sack.clear()  # dump everything out

    # put items in knapsack until full
    weight = 0

    for i in items:
        weight_remaining = 50 - weight

        if i.weight <= weight_remaining:
            sack.append(i)
            weight += i.weight

    return sack


def brute_force_fill_knapsack(sack, items):
    """Try every combo to find the best"""
    sack.clear()
    # generate all possible combinations of items
    combos = []

    for i in range(1, len(items) + 1):
        list_of_combos = list(combinations(items, i))

        for combo in list_of_combos:
            combos.append(list(combo))

    # calculate the value of all combinations
    best_value = -1

    for combo in combos:
        value = 0
        weight = 0

        for item in combo:
            value += item.value
            weight += items.weight

        # find the combo w/ the highest value
        if weight <= 50 and value > best_value:
            best_value = value
            sack = combo

    return sack


# 0(n log n)
def greedy_fill_knapsack(sack, items):
    """Use ratio of [value] / [weight] to choose items"""
    # calculate efficiencies
    for i in items:  # O(n) over the # of items
        i.efficiency = i.value / i.weight

    # sort items by efficiency

    #     def sort_func(el):
    #          return el.efficiency
    #      items.sort(key=sort_func, reverse=True)

    # lambda is anon func, reverse=True is descending order
    items.sort(key=lambda el: el.efficiency, reverse=True)  # O(log n)

    sack.clear()  # dump everything out

    # put items in knapsack until full
    weight = 0

    for i in items:  # O(n) over the # of items
        weight_remaining = 50 - weight

        if i.weight <= weight_remaining:
            sack.append(i)
            weight += i.weight

    return sack


fill_cave_with_items()
knapsack = []

# Test 1 Naive
print("\nStarting test 1, naive approach...")
items = large_cave
start = time.time()
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# Test 2 - Brute Force
print("Starting test 2, brute force...")
items = medium_cave
start = time.time()
knapsack = brute_force_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# THIS WILL TAKE ~FOREVER~ TO RETURN 0(n!)
# # Test 3 - Brute Force
# print('Starting test 3, brute force...')
# items = large_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results (items, knapsack)

# Test 4 - Greedy
print("Starting test 4, greedy approach...")
items = medium_cave
start = time.time()
greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# Test 5 - Greedy
print("Starting test 5, greedy approach...")
items = large_cave
start = time.time()
greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)
