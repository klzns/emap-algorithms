class Node:
    def __init__(self, cargo=None, next=None):
        # Value of the node
        self.car = cargo
        # Link to the next element in the list
        self.cdr = next

    # Return the distance of the node until the other
    # This method assumes that the list has unique elements
    # E.g. if used on the first element of the list with the second parameter
    # as None it will return the length of the list
    def distance(self, end_node):
        node = self
        has_next = None
        length = 0

        length = length + 1
        while node.cdr and node.car is not end_node:
            node = node.cdr
            length = length + 1

        return length


# Transform an array to a linked list
class List:
    def __init__(self, values):
        first = None
        previous_node = None

        for value in values:
            # Link the previous node with the current node
            if previous_node:
                previous_node.cdr = node = Node(value)
            # In case is the first node of the list
            else:
                node = Node(value)
                first = node

            previous_node = node

        # The only attribute this object has is a link to the first element
        self.first = first
