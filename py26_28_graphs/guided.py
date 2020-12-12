class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


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


class Graph:
    def __init__(self):
        self.vertices = {}  # keys == all verts, val == sets of adj verts

    def add_vertex(self, vertex):
        """Add a new unconnected vert"""
        self.vertices[vertex] = set()

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("Non-existent vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("Non-existent vertex")

    def get_neighbors(self, v):
        return self.vertices[v]

    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex_id)  # init

        while q.size() > 0:  # while our queue isn't empty
            v = q.dequeue()

            if v not in visited:
                print(v)  # "visit" the vertex (node)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        s = Stack()
        visited = set()

        s.push(starting_vertex_id)

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                print(v)  # "visit" the vertex (node)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def bfs(self, starting_vertex_id, target_vertex_id):
        pass
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
        #   Dequeue the first PATH
        #   Grab the last vertex from the PATH
        #   If that vertex has not been visited...
        #           CHECK IF IT'S THE TARGET
        #           IF so, RETURN PATH
        #       Mark it as visited...
        #       Then add A PATH TO its neighbors to the back of the queue
        #           COPY THE PATH
        #           APPEND THE NEIGHOR TO THE BACK


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print()
print(g.vertices)

print()
g.bft(1)
print()
g.dft(1)