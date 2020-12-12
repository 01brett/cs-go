import random
import re

# Read in all the words in one go
with open("markov5/input.txt") as f:
    words = f.read().split()

store = {}
starts = []


# analyze which words can follow other words
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in store:
        store[word] = []

    store[word].append(next_word)

    if re.match('^[A-Z]|^\"[A-Z]]', word):
        starts.append(word)

# construct 5 random sentences

for i in range(5):
    w = random.choice(starts)
    print(w, end=" ")

    while re.search('[\.\?\!]\"$|[\.\?\!]$', w) is None:
        w = random.choice(store[w])
        print(w, end=" ")

    print("\n")
