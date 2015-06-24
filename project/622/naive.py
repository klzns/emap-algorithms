def is_there_sum(list_of_values, t):
    # Se o valor de t for negativo, e impossivel, pois a lista admite apenas
    # valores positivos
    if t < 0:
        return False
    # Como caso inicial, e sempre possivel escolher o subconjunto vazio para
    # sua soma dar zero
    if t == 0:
        return True
    # Se a lista possuir apenas um elemento e ele for igual a soma pedida,
    # obviamente o subconjunto pedido existe
    elif len(list_of_values) == 1 and list_of_values[0] == t:
        return True
    # Caso a lista seja unitaria e nao igual ao elemento da soma, nao existe o
    # subconjunto pedido
    elif len(list_of_values) == 1 and list_of_values[0] != t:
        return False
    # Nao retirando o ultimo elemento da lista, ou ele participara do
    # subconjunto pedido, ou nao
    else:
        last = list_of_values[-1]
        new_list = list_of_values[:-1]
        return is_there_sum(new_list, t-last) or is_there_sum(new_list, t)


def main():
    set = [3, 34, 4, 12, 5, 2]
    t = 9

    if is_there_sum(set, t) is True:
        print "Found a subset with a given sum"
    else:
        print "No subset with a given sum"
    return True


if __name__ == '__main__':
    main()
