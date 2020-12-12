import re


def word_count(s):
    count = {}
    if s == "":
        return count
    # split the words out from sentence
    words = s.split()
    # loop over split words array
    for word in words:
        # clean out extra junk
        w = re.sub(r"[\"\:\;\,\.\-\+\=\/\\\|\[\]\{\}\(\)\*\^\&]", "", word).lower()
        if w == "":
            continue
        if w not in count:
            count[w] = 0

        count[w] += 1

    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )
