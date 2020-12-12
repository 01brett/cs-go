# Your code here


def finder(files, queries):
    result = []
    cache = {q: True for q in queries}

    for file in files:
        temp = file.split("/")
        target = temp[-1]
        if target in cache:
            result.append(file)

    return result


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
