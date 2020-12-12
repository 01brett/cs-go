# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("crack_caesar7/ciphertext.txt") as f:
    txt = f.read()

char_count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0,
}
count = 0

for char in txt:
    # if it's not a letter, skip to next loop cycle
    if char not in char_count:
        continue

    char_count[char] += 1
    count += 1
# turn our dict into a list of tuples
freq = list(char_count.items())
# sort our tuples by 2nd el, descending (big -> small)
freq.sort(key=lambda el: -el[1])

freq_list = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]
decoder = {}

for i in range(len(freq)):
    scrambled_letter = freq[i][0]
    decoded_letter = freq_list[i]
    decoder[scrambled_letter] = decoded_letter

decoded_txt = ""

for char in txt:
    if char in decoder:
        decoded_txt += decoder[char]
    else:
        decoded_txt += char

print(decoded_txt)
