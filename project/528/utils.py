import csv


def read_csv(filename):
    people = []
    matrix = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            people.append(row[0])
            matrix.append(row[1:])

    return [people, matrix]


def verify_matrix(matrix):
    matrix_len = len(matrix)
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] is not matrix[j][i]:
                print 'Something is wrong at '+str(i)+', '+str(j)
                return False
    return True


def add_person_once(destination, source):
    for item in source:
        try:
            destination.index(item)
        except ValueError:
            destination.append(item)

    return destination


def find_person_index(people, person_name):
    for index, person in enumerate(people):
        if person == str(person_name):
            return index
    return None
