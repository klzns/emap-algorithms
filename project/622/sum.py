

# Funcao que printa uma matriz gerada por programacao dinamica
def print_subset(subset, n, t):
    for i in range(0, t+1):
        to_print = ""
        for j in range(0, n+1):
            to_print += str(subset[i][j]) + "\t"
        print to_print


def is_subset_sum(set, t):
    n = len(set)
    subset = []
    for i in range(0, t+1):
        array = []
        for j in range(0, n+1):
            array.append([])
        subset.append(array)
    # Casos base:
    # Se a soma e zero a resposta e True
    for i in range(0, n+1):
        subset[0][i] = True

    # Se a soma e diferente de zero e o conjunto vazio, a resposta e False
    for i in range(1, t+1):
        subset[i][0] = False
    # Construir matriz com os valores pra cada lista e para cada t
    for i in range(1, t+1):
        for j in range(1, n+1):
            subset[i][j] = subset[i][j-1]

            if i >= set[j-1]:
                subset[i][j] = subset[i][j] or subset[i - set[j-1]][j-1]
    # Mostrar a matriz da programacao dinamica
    print_subset(subset, n, t)

    return subset[t][n]


def main():
    set = [3, 34, 4, 12, 5, 2]
    t = 9

    if is_subset_sum(set, t) is True:
        print "Found a subset with a given sum"
    else:
        print "No subset with a given sum"
    return True


if __name__ == '__main__':
    main()
