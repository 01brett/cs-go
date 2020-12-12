def no_dups(s):
    if s == "":
        return s

    words = s.split()

    if len(words) < 2:
        return s

    dedup = []
    seen = {}

    for word in words:
        if word not in seen:
            seen[word] = True
            dedup.append(word)

    return " ".join(dedup)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
