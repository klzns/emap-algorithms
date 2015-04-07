class Node:
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.cdr = next

    def __str__(self):
        return str(self.car)

    def distance(self, end_value):
        node = self
        has_next = None
        length = 0

        length = length + 1
        while node.cdr and node.car is not end_value:
            node = node.cdr
            length = length + 1

        return length


class List:
    def __init__(self, values):
        first = None
        oldNode = None

        for value in values:
            if oldNode:
                oldNode.cdr = node = Node(value)
            else:
                node = Node(value)

            if first is None:
                first = node

            oldNode = node

        self.first = first
