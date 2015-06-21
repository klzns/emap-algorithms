import csv


def read_csv(filename):
    vertices = []
    edges = []
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            if i == 0:
                vertices = row
                continue
            edges.append(row)

    edges_mapped = []
    for i, edge in enumerate(edges):
        for j, col in enumerate(edge):
            if col != "0":
                edge_prop = {
                    'from': vertices[i],
                    'to': vertices[j],
                    'cost': int(col)
                }
                edges_mapped.append(edge_prop)

    return [vertices, edges_mapped]
