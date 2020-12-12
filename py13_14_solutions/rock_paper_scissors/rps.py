#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    rps = ["rock", "paper", "scissors"]

    ans = []

    def inner(n):
        for i in range(3 ^ n):
            temp = []

            ans.append(temp)

    return ans


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
