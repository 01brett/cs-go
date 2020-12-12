import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

dupes = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             dupes.append(name_1)
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # go left
        if value < self.value:
            # base case
            if self.left is None:
                self.left = BSTNode(value)
                return
            self.left.insert(value)
        # go right
        else:
            # base case
            if self.right is None:
                self.right = BSTNode(value)
                return
            self.right.insert(value)

    def contains(self, target):
        # base case
        if target == self.value:
            return True
        # go left
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        # go right
        else:
            if self.right:
                return self.right.contains(target)
        # target not found
        return False


bst = BSTNode("_")
for name1 in names_1:
    bst.insert(name1)
for name2 in names_2:
    if bst.contains(name2):
        dupes.append(name2)

end_time = time.time()

print(f"{len(dupes)} duplicates:\n\n{', '.join(dupes)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# dupes = list(set(names_1).intersection(set(names_2)))
