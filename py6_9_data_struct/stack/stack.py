"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList

"""
Using my Linked List
"""


class Stack:
    def __init__(self):
        self.storage = LinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


"""
Using Python lists
"""


class StackPythonLists:
    def __init__(self):
        self.storage = []
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size = len(self.storage)

    def pop(self):
        ret_val = self.storage.pop() if self.size > 0 else None
        self.size = len(self.storage)
        return ret_val
