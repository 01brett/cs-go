"""
____________________

Connected Components
____________________

Separate "islands" in a graph

Example:

graph nodes: A B C D E F
graph edges: A,B C,D C,E D,E
"""

islands1 = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
]


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


def island_counter(islands):
    visited = set()
    count = 0

    def get_neighbors(coords):
        neighbors = []
        row, col = coords

        if row > 0 and islands[row - 1][col] == 1:
            neighbors.append((row - 1, col))

        if row < len(islands) - 1 and islands[row + 1][col] == 1:
            neighbors.append((row + 1, col))

        if col > 0 and islands[row][col - 1] == 1:
            neighbors.append((row, col - 1))

        if col < len(islands) - 1 and islands[row][col + 1] == 1:
            neighbors.append((row, col + 1))

        return neighbors

    def bft(row, col):
        q = [(row, col)]

        while len(q) > 0:
            coords = q.pop(0)

            if (coords) not in visited:
                visited.add(coords)

                for neighbor in get_neighbors(coords):
                    q.append(neighbor)

    # for all nodes in graph
    for row in range(len(islands)):
        for col in range(len(islands[row])):
            node_val = islands[row][col]
            coords = (row, col)
            # if we find unvisted 1 node
            if node_val == 1 and coords not in visited:
                bft(row, col)  # bft from that node
                count += 1  # inc our count

    return count


print(island_counter(islands1))  # returns 4
