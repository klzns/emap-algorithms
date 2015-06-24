def is_there_a_graph(array):
    ind = 0
    while ind == 0:
        # Ordenar a lista
        array.sort()
        array.reverse()

        # Casos iniciais
        if len(array) == 2:
            if array[0] == array[1] == 0 or array[0] == array[1] == 1:
                return True
            else:
                return False
        # Reducao do problema usando o Lema
        else:
            ini = array[0]
            array = array[1:]
            if len(array) < ini:
                return False
            else:
                for i in range(ini):
                    array[i] = array[i] - 1
                print array


def main():
    list = [2, 3, 4, 3, 5, 3, 2, 2, 4, 3, 3]

    print 'Testing a graph that exists'
    print list
    print is_there_a_graph(list)

    list = [2, 3, 4, 3, 5, 3, 2, 2, 4, 3, 10]

    print '\nTesting a wrong entry'
    print list
    print is_there_a_graph(list)


if __name__ == '__main__':
    main()
