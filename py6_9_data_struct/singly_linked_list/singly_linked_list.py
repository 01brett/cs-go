class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)

        # empty list
        if self.head is None:
            # update head and tail attributes
            self.head = self.tail = new_node
            return

        # set next_node of my new Node to the head
        new_node.set_next(self.head)
        # update the List head attr to our new Node
        self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)

        # list is empty
        if self.head is None:
            self.head = self.tail = new_node
            return

        # list is not empty
        self.tail.set_next(new_node)
        self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None

        ret_val = self.head.get_value()

        # list of 1
        if self.head is self.tail:
            self.head = self.tail = None
            return ret_val

        # list > 1 element
        self.head = self.head.get_next()

        return ret_val

    def remove_tail(self):
        # list len == 0
        if self.head is None:
            return None

        ret_val = self.tail.get_value()

        # list len == 1
        if self.head is self.tail:
            self.head = self.tail = None
            return ret_val

        # list len > 1
        temp = self.head
        while temp.get_next() is not self.tail:
            temp = temp.get_next()

        temp.set_next(None)
        self.tail = temp

        return ret_val

    def contains(self, value):
        temp = self.head
        # loop thru list until temp node is None
        while temp is not None:
            if temp.get_value() == value:
                return True

            temp = temp.get_next()
        return False

    def get_max(self):
        # empty list
        if self.head is None:
            return None

        # list == 1
        elif self.head is self.tail:
            return self.head.get_value()

        # list > 1
        temp = self.head
        max_val = self.head.get_value()

        while temp is not None:
            if temp.get_value() > max_val:
                max_val = temp.get_value()

            temp = temp.get_next()
        return max_val
