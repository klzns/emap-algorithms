
class Node:
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.cdr = next

    def __str__(self):
        return str(self.car)


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


def linked_list_len(node, end_value):
    has_next = None
    length = 0
    if node is None:
        return length

    length = length + 1
    while node.cdr and node.car is not end_value:
        node = node.cdr
        length = length + 1

    return length


def find_index(first_node, end_value, index):
    length = linked_list_len(first_node, end_value)
    middle = length/2 - 1
    index = index + middle

    if length is 1:
        if first_node.car is index:
            return index
        else:
            return None

    i = 0
    node = first_node
    while i != middle:
        node = node.cdr
        i = i + 1

    if node.car is index:
        return index
    elif node.car > index:
        return find_index(first_node, node.car, 0)
    elif node.car < index:
        return find_index(node, None, middle)

if __name__ == '__main__':
    list = [0, 1, 2, 3, 4, 5]
    ll = List(list)

    index = find_index(ll.first, None, 0)

    if index is not None:
        print 'Found! Index: ' + str(index)
    else:
        print 'No match was found.'
