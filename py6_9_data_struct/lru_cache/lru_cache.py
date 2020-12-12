class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node


class MyList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_node(self, node):
        # empty list
        if self.head is None:
            self.head = self.tail = node
        else:
            # non-empty list
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def detach_oldest(self):
        # grab ref to tail
        node = self.tail
        # make 2nd oldest the new tail
        self.tail = node.prev
        self.tail.next = None
        # sever prev pointer on old tail
        node.prev = None
        # return old
        self.length -= 1
        return node

    def make_newest(self, node):
        # head case
        if node is self.head:
            return
        # tail case
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = node.next
        # move pointers surrounding target node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # reassign head
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.dll = MyList()
        self.dict = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.dict:
            return None

        node = self.dict[key]
        self.dll.make_newest(node)

        return node.value[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, val):
        # for overwrites
        if key in self.dict:
            node = self.dict[key]
            node.value[key] = val
            self.dll.make_newest(node)
            return

        # if at limit, delete oldest
        if len(self.dll) == self.limit:
            oldest = self.dll.detach_oldest()
            old_key = list(oldest.value)[0]
            del self.dict[old_key]

        # create node
        new_node = Node({key: val})
        # add to dict and list
        self.dict[key] = new_node
        self.dll.add_node(new_node)
