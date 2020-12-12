def intersection(arrays):
    cache = {}
    result = []
    num_of_arrays = len(arrays)

    for arr in arrays:
        for num in arr:
            if num not in cache:
                cache[num] = 0
            cache[num] += 1
            # check if this number has been found in all lists
            if cache[num] == num_of_arrays:
                result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
