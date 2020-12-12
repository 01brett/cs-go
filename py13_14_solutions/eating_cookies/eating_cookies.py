"""
Input: an integer
Returns: an integer
"""

cache = {}


def eating_cookies(n):
    # base case
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        x = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        cache[n] = x
        return x


# def eating_cookies(n):
#     # base case
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     # recursion
#     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 50

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
