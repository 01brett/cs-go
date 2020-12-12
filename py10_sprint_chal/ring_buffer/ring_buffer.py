from typing import ItemsView


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.cur = -1

    def append(self, item):
        # at capacity
        if len(self.store) == self.capacity:
            self.cur = (self.cur + 1) % self.capacity
            self.store[self.cur] = item
        # under capacity
        else:
            self.store.append(item)

    def get(self):
        return self.store
