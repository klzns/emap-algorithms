import sys
from console import print_status, print_result, print_instructions
from utils import read_csv, verify_edges, find_person_index, get_edges_of_person


# Essa funcao lista as pessoas que nao atendem as retricoes de amizade minima e
# e de desconhecidos minimos
def filter_people(people, edges, minimum_number_of_friends, must_not_know_at_least):
    # Numero total de pessoas
    number_of_people = len(people)

    people_to_remove = []

    for i, person in enumerate(people):
        # Verifica quantos amigos ela tem
        edges_of_person = get_edges_of_person(people, edges, person)
        friends = len(edges_of_person)

        # Caso tenha menos amigos do que o minimo estabelecido
        if friends < minimum_number_of_friends:
            # Ela entra na lista
            people_to_remove.append(person)

        # Caso ela tenha mais amigos do que o numero total de pessoas menos
        # o minimo de desconhecidos
        if friends >= len(people) - must_not_know_at_least:
            # Ela entra na lista
            people_to_remove.append(person)

    return people_to_remove


def remove_person(people, edges, person_name):
    new_people = people[:]
    new_edges = edges[:]

    # Pegamos o indice dessa pessoa na matriz de incidencia
    person_index = find_person_index(people, person_name)

    for i, edge in enumerate(new_edges):
        # Caso a aresta seja relacionada a pessoa
        if edge[person_index] == "1":
            # Retiramos a aresta
            new_edges.pop(i)

    # Retiramos a pessoa da lista de pessoas
    new_people.pop(person_index)

    return [new_people, new_edges]


# Removemos as pessoas que estao na lista
def remove_people(people, edges, list):
    new_people = people[:]
    new_edges = edges[:]

    for person in list:
        [new_people, new_edges] = remove_person(new_people, new_edges, person)

    return [new_people, new_edges]


def main(min_friends, min_strangers):
    people, edges = read_csv('friends.csv')

    # Se algo esta errado na matriz de incidencia, aborta
    if verify_edges(edges) is False:
        return

    iteration = 1
    while True:
        # Pegamos as pessoas que nao atendem as restricoes, isto eh,
        # que nao possuem no minimo 5 amigos e que nao desconhecem pelo menos
        # outras 5
        people_to_remove = filter_people(people, edges, min_friends, min_strangers)
        people_to_remove = set(people_to_remove)

        # Quando nao tivermos mais ninguem para retirar da lista, paramos o algoritmo
        if len(people_to_remove) is 0:
            break

        # Removemos as pessoas que nao atendem as restricoes
        [people, edges] = remove_people(people, edges, people_to_remove)

        # Imprimimos o estado atual da lista de convidados
        print_status(people, edges, people_to_remove, iteration)

        iteration += 1

    # Imprimimos o resultado
    print_result(people)


if __name__ == '__main__':
    # Numero minimo de amigos na festa
    minimum_number_of_friends = 5
    # Numero minimo de desconhecidos na festa
    must_not_know_at_least = 5

    if len(sys.argv) is 3:
        minimum_number_of_friends = int(sys.argv[1])
        must_not_know_at_least = int(sys.argv[2])
    else:
        print_instructions()

    main(minimum_number_of_friends, must_not_know_at_least)
