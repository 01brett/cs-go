"""
Given two words (begin_word and end_word), and a dictionary's word list, return
the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.

Each transformed word must exist in the word list. Note that begin word is not
transformed word.

Note:

Return `None` if there is no such transformation sequence.
All words (starting, ending, dictionary) contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end word are non-empty and are not the same.

Examples:

begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word "sail"
end_word = "boat"
return: ['sail', 'bail', boil', 'boll', 'bolt', 'boat']

begin_word = "hungry"
end_word = "happy"
return: None
"""

# "shortest transformation sequence" -> we should be thinking... breadth-first search in a graph!

words = set()

with open("words.txt") as f:
    for w in f:
        w = w.strip()
        words.add(w)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def get_neighbors1(word):
    neighbors = []

    for w in words:  # O(n) over the number of words in set -> 64,000
        if len(w) != len(word):
            continue

        diff = 0
        for i in range(len(w)):  # O(n) over the length of word
            if w[i] != word[i]:
                diff += 1
            if diff > 1:
                break
        if diff == 1:
            neighbors.append(w)
    return neighbors


import string


def get_neighbors(word):  # this variant is faster
    neighbors = []

    letters = list(string.ascii_lowercase)
    word_letters = list(word)

    for i in range(len(word_letters)):  # 0(n) length of word
        for l in letters:  # 0(26) all lowercase letters
            word_copy = list(word_letters)
            word_copy[i] = l
            new_word = "".join(word_copy)

            if new_word != word and new_word in words:
                neighbors.append(new_word)

    return neighbors


def bfs(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = path + [neighbor]
                q.enqueue(path_copy)


print(bfs("hungry", "happy"))
print(bfs("hit", "cog"))
print(bfs("sail", "boat"))
print(bfs("poor", "rich"))
