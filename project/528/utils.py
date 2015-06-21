import csv


def read_csv(filename):
    people = []
    edges = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            if i == 0:
                people = row
                continue
            edges.append(row)

    return [people, edges]


def verify_edges(edges):
    for i, edge in enumerate(edges):
        count = []
        for j, col in enumerate(edge):
            if col == "1":
                count.append(j)
            if len(count) > 2:
                print 'Something is wrong at edge '+str(i)
                print count
                print ''
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


def get_edges_of_person(people, edges, person_name):
    person_index = find_person_index(people, person_name)

    person_edges = []
    for i, edge in enumerate(edges):
        if edge[person_index] == "1":
            person_edges.append(i)

    return person_edges
