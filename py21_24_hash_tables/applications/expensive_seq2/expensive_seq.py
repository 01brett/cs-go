def expensive_seq(x, y, z):
    cache = {}

    def recurse(x, y, z):
        if x <= 0:
            return y + z

        key = (x, y, z)

        if key not in cache:
            cache[key] = (
                recurse(x - 1, y + 1, z)
                + recurse(x - 2, y + 2, z * 2)
                + recurse(x - 3, y + 3, z * 3)
            )
        return cache[key]

    return recurse(x, y, z)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i * 2, i * 3, i * 4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
