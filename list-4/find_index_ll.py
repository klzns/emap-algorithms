# Find in a linked list, a, of ordered unique integers if exists an element
# that a[i] is i
from linked_list import List


def find_index(first_node, end_node, index):
    # Get linked list length
    length = 0
    if first_node is not None:
        length = first_node.distance(end_node)

    # Get middle index
    middle = length/2 - 1
    # Sum with the index of the start of the list
    index = index + middle

    # Base case
    if length is 1:
        # If a[i] is i
        if first_node.car is index:
            return index
        else:
            return None

    # Let's walk the list until we find the middle node
    i = 0
    node = first_node
    while i != middle:
        node = node.cdr
        i = i + 1

    # If a[i] is i
    if node.car is index:
        return index
    # a[i] is bigger, check left hand side of the list
    elif node.car > index:
        return find_index(first_node, node.car, 0)
    # a[i] is smaller, check right hand side of the list
    elif node.car < index:
        return find_index(node, None, middle)

if __name__ == '__main__':
    # Example list
    list = [0, 1, 2, 3, 4, 5]
    # Make it a linked list
    ll = List(list)

    index = find_index(ll.first, None, 0)

    if index is not None:
        print 'Found! Index: ' + str(index)
    else:
        print 'No match was found.'
