import re


def histo(s):
    with open(f"histo6/{s}") as f:
        words = f.read().split()

    count = {}
    longest_word = 0

    for word in words:
        # clean out extra junk
        w = re.sub(r"[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&\?\!]", "", word).lower()

        if w == "":
            continue

        if w not in count:
            count[w] = 0

        count[w] += 1

        if len(w) > longest_word:
            longest_word = len(w)

    arr = list(count.items())
    arr.sort(key=lambda el: (-el[1], el[0]))

    for el in arr:
        word = el[0]
        word_count = el[1]
        if word_count >= 6:
            space = longest_word - len(word)
            print(f"{word}{' ' * space}  {'#' * word_count}")


histo("robin.txt")
