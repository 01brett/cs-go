def has_negatives(arr):
    result = []
    cache = {}
    for n in arr:
        if n == 0:  # handle edge case for 0
            continue
        if n not in cache:
            cache[n] = True

        if -n in cache:
            result.append(abs(n))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
