import sys
from console import print_status, print_result, print_instructions
from utils import read_csv, verify_edges, add_person_once, find_person_index, get_edges_of_person


def filter_people(people, edges, minimum_number_of_friends, must_unknow_at_least):
    number_of_people = len(people)

    has_too_few_friends = []
    has_too_much_friends = []

    for i, person in enumerate(people):
        edges_of_person = get_edges_of_person(people, edges, person)

        friends = len(edges_of_person)

        if friends < minimum_number_of_friends:
            has_too_few_friends.append(person)

        if friends >= len(people) - must_unknow_at_least:
            has_too_much_friends.append(person)

    return [has_too_few_friends, has_too_much_friends]


def remove_person(people, edges, person_name):
    new_people = people[:]
    new_edges = edges[:]

    person_index = find_person_index(people, person_name)
    person_edges = get_edges_of_person(people, edges, person_name)

    while True:
        removed = False
        for i, edge in enumerate(edges):
            if edge[person_index] == "1":
                edges.pop(i)
                removed = True
                break
        if removed is False:
            break

    new_people.pop(person_index)

    return [new_people, new_edges]


def remove_people(people, edges, list):
    new_people = people
    new_edges = edges
    for person in list:
        [new_people, new_edges] = remove_person(new_people, new_edges, person)

    return [new_people, new_edges]


def main(mininum, max):
    people, edges = read_csv('friends.csv')
    if verify_edges(edges) is False:
        return

    iteration = 1
    while True:
        people_to_remove = []
        [has_too_few_friends, has_too_much_friends] = filter_people(people, edges, mininum, max)
        people_to_remove.extend(has_too_few_friends)
        people_to_remove = add_person_once(people_to_remove, has_too_much_friends)

        if len(people_to_remove) is 0:
            break

        [people, edges] = remove_people(people, edges, people_to_remove)
        print_status(people, edges, people_to_remove, iteration)

        iteration += 1

    print_result(people)


if __name__ == '__main__':
    minimum_number_of_friends = 5
    must_unknow_at_least = 5

    if len(sys.argv) is 3:
        minimum_number_of_friends = int(sys.argv[1])
        must_unknow_at_least = int(sys.argv[2])
    else:
        print_instructions()

    main(minimum_number_of_friends, must_unknow_at_least)
