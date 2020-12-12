class HashTableNode:
    """
    Linked List hash table node key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableList:
    """
    Linked list to manage head reference
    """

    def __init__(self):
        self.head = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string key
    """

    def __init__(self, capacity):
        self.capacity = max(capacity, MIN_CAPACITY)
        self.storage = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        return self.load / self.capacity

    def fnv1(self, key):
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed = FNV_offset_basis

        key_bytes = key.encode()
        for byte in key_bytes:
            hashed = hashed * FNV_prime
            hashed = hashed ^ byte  # XOR bitwise operation

        return hashed

    def djb2(self, key):
        hashed = 5381

        key_bytes = key.encode()

        for byte in key_bytes:
            hashed = (hashed << 5) + byte  # bitwise left shift
            # hashed = (hashed * 33) + byte

        return hashed

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        load_factor = self.get_load_factor()
        if load_factor > 0.7:
            capacity = self.capacity * 2
            self.resize(capacity)

        idx = self.hash_index(key)
        # idx linked list is empty
        if self.storage[idx] is None:
            # init new linked list
            self.storage[idx] = HashTableList()
            ll = self.storage[idx]
            # add entry to linked list
            new_entry = HashTableNode(key, value)
            # assigned new_entry to head/tail (since list is empty)
            ll.head = new_entry
            self.load += 1
            return
        # idx linked list is not empty
        ll = self.storage[idx]
        new_entry = HashTableNode(key, value)
        # loop through linked list to see if we overwrite
        cur_node = ll.head
        while cur_node is not None:
            # if we have the key, overwrite the value
            if cur_node.key == key:
                cur_node.value = value
                return
            # if the cur_node is the tail, add new_entry as new tail
            if cur_node.next is None:
                cur_node.next = new_entry
                self.load += 1
                return
            # continue traversal
            cur_node = cur_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        idx = self.hash_index(key)

        if self.storage[idx] == None:
            print("Warning: key not found")
            return

        # idx linked list is not empty
        ll = self.storage[idx]
        # loop through linked list
        prev_node = None
        cur_node = ll.head
        while cur_node is not None:
            # if we have the key
            if cur_node.key == key:
                if prev_node is None and cur_node.next is None:
                    ll.head = None
                elif prev_node is None and cur_node.next:
                    ll.head = cur_node.next
                else:
                    prev_node.next = cur_node.next
                self.load -= 1
                return
            # continue traversal
            prev_node = cur_node
            cur_node = cur_node.next
        # we never found it
        print("Warning: key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        idx = self.hash_index(key)
        if self.storage[idx] is not None:
            # idx linked list is not empty
            ll = self.storage[idx]
            # loop through linked list to find our target
            cur_node = ll.head
            while cur_node is not None:
                # if we find our target, return it's value
                if cur_node.key == key:
                    return cur_node.value
                # continue traversal
                cur_node = cur_node.next
        # we never found our target
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        # capture old storage
        old_store = self.storage
        old_load = self.load
        # reassign props with new values to allow us to use methods
        self.capacity = new_capacity
        self.storage = [None] * self.capacity
        # set load to unoffensive number
        self.load = 0.4
        # loop thru old store to grab and rehash everything
        for i in old_store:
            if i is None:  # this index was empty
                continue
            cur_node = i.head
            while cur_node is not None:
                self.put(cur_node.key, cur_node.value)
                # negate the load we just added
                self.load -= 1
                cur_node = cur_node.next
        # reassert the old load number now we've resized
        self.load = old_load


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
