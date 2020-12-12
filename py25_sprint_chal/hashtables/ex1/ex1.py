def get_indices_of_item_weights(weights, length, limit):
    if length < 2:
        return None

    cache = {}
    for idx in range(length):
        weight = weights[idx]

        diff = limit - weight

        if diff in cache:
            return tuple([idx, cache[diff][-1]])

        if weight not in cache:
            cache[weight] = [idx]  # to prevent dup'd weight overwriting
        else:
            cache[weight].append(idx)

    return None
