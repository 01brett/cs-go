def fib(n):  # bottom up dynamic programming
    f = [0, 1]

    if n <= 1:
        return f[n]

    for _ in range(2, n + 1):
        next_fib = f[-1] + f[-2]
        f.append(next_fib)

    return f[-1]


def fib1(n):
    result = 0
    n_1 = 1
    n_2 = 0

    for _ in range(n - 1):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result

    return result


# for i in range(10):
#     print(fib(i))

words = []

with open("words.txt") as f:
    for w in f:
        w = w.strip()
        words.append(w)


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


def anagrams():
    ans = {}

    longest_sig = None
    longest_len = -1

    for w in words:  # 0(n) over the # of words
        sig = "".join(sorted(w))

        if sig not in ans:
            ans[sig] = []

        ans[sig].append(w)

        if len(ans[sig]) > longest_len:
            longest_len = len(ans[sig])
            longest_sig = sig

    return ans[longest_sig]


print(anagrams())
