# Find the bigger element in a list
from linked_list import List


# Codigo para o peak entry - array
def peak_entry_array(a):
    size = len(a)
    m = size/2
    if size == 1 or size == 0:
        return a[0]
    if size == 2:
        return max(a[0], a[1])

    a_l = a[:m]
    a_r = a[m:]
    meio = a[m]

    af1 = meio > a[m-1]
    af2 = meio > a[m+1]

    if af1 and af2:
        return meio
    elif af1 and not(af2):
        return peak(a_r)
    elif af2 and not(af1):
        return peak(a_l)


# Codigo para o peak - Lista encadeada
def peak_entry_ll(first_node, end_node, index):
    size = 0
    if first_node is not None:
        size = first_node.distance(end_node)

    m = size/2 - 1

    if size == 1 or size == 0:
        return first_node.car
    if size == 2:
        return (max(first_node.car, first_node.cdr.car))

    i = 0
    node = first_node
    while i != m+1:
        prenode, node = node, node.cdr
        i += 1

    af1 = node.car > prenode.car
    af2 = node.car > node.cdr.car
    if af1 and af2:
        return node.car
    elif af1 and not(af2):
        return peak_enc(node, None, m)
    elif af2 and not(af1):
        return peak_enc(first_node, node.car, 0)

if __name__ == '__main__':
    # Lista de exemplo list
    list = [0, 2, 3, 4, 2, 1]

    # Make it a linked list
    ll = List(list)
    value = peak_entry_ll(ll.first, None, 0)

    print 'Linked List'
    if value is not None:
        print 'Found: Peak is ' + str(value) + '!'
    else:
        print 'No match was found.'
    print ''

    value = peak_entry_array(list)

    print 'Array'
    if value is not None:
        print 'Found: Peak is ' + str(value) + '!'
    else:
        print 'No match was found.'
