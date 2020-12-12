# memoization closely related to dynamic programming
## DP: top down, break the problem down as you go
## reuse previous results


def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def memo_fib(n):
    cache = {}

    def recurse(n):
        if n <= 1:
            return n

        if n not in cache:
            cache[n] = recurse(n - 1) + recurse(n - 2)

        return cache[n]

    return recurse(n)


print(fib(3))
print(fib(6))
print(memo_fib(400))
