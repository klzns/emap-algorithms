
def find_index(list, index):
    length = len(list)
    middle = length/2 - 1
    index = index + middle

    if length is 1:
        if list[0] is index:
            return index
        else:
            return None

    middle_node = list[middle]

    if middle_node is index:
        return index
    elif middle_node > index:
        return find_index(list[:middle], 0)
    elif middle_node < index:
        return find_index(list[middle:], middle)


if __name__ == '__main__':
    list = [0, 1, 2, 3, 4, 5]

    index = find_index(list, 0)

    if index is not None:
        print 'Found! Index: ' + str(index)
    else:
        print 'No match was found.'
