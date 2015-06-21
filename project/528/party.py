import sys
from console import print_status, print_result, print_instructions
from utils import read_csv, verify_matrix, add_person_once, find_person_index


def filter_people(people, matrix, minimum_number_of_friends, must_unknow_at_least):
    number_of_people = len(matrix)

    has_too_few_friends = []
    has_too_much_friends = []

    for i, row in enumerate(matrix):
        friends = 0
        for col in row:
            if int(col) is 1:
                friends = friends + 1

        if friends < minimum_number_of_friends:
            has_too_few_friends.append(people[i])

        if friends + must_unknow_at_least > number_of_people:
            has_too_much_friends.append(people[i])

    return [has_too_few_friends, has_too_much_friends]


def remove_person(people, matrix, person_name):
    new_people = people[:]
    new_matrix = matrix[:]

    person_index = find_person_index(people, person_name)

    new_matrix.pop(person_index)
    new_people.pop(person_index)

    for row in new_matrix:
        row.pop(person_index)

    return [new_people, new_matrix]


def remove_people(people, matrix, list):
    new_people = people
    new_matrix = matrix
    for person in list:
        [new_people, new_matrix] = remove_person(new_people, new_matrix, person)

    return [new_people, new_matrix]


def main(mininum, max):
    people, matrix = read_csv('friends.csv')
    verify_matrix(matrix)

    iteration = 1
    while True:
        people_to_remove = []
        [has_too_few_friends, has_too_much_friends] = filter_people(people, matrix, mininum, max)
        people_to_remove.extend(has_too_few_friends)
        people_to_remove = add_person_once(people_to_remove, has_too_much_friends)

        if len(people_to_remove) is 0:
            break

        [people, matrix] = remove_people(people, matrix, people_to_remove)
        print_status(people, matrix, people_to_remove, iteration)

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
