import csv
import networkx as nx
import matplotlib.pylab as plt


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


def find_edge(edges, frm, to):
    for edge in edges:
        if edge['from'] == frm and edge['to'] == to:
            return edge
    return None


def show_path(path, vertices, edges, v0):
    graph = nx.DiGraph()

    for vertex in vertices:
        graph.add_node(vertex)

    edges = edges[:]
    path = path[::-1]
    for i, node in enumerate(path):
        if i > 0:
            edge = find_edge(edges, path[i-1], node)
            if edge is None:
                continue
            if edge['from'] == path[i-1] and edge['to'] == node:
                edge['path'] = True
                continue

    for edge in edges:
        if 'path' not in edge:
            edge['path'] = False
        graph.add_edge(edge['from'], edge['to'], weight=edge['cost'], cost=edge['path'])

    edefault = [(u, v) for (u, v, d) in graph.edges(data=True) if not d['cost']]
    epath = [(u, v) for (u, v, d) in graph.edges(data=True) if d['cost']]
    edge_labels = dict([((u, v, ), d['weight']) for (u, v, d) in graph.edges(data=True)])

    pos = nx.circular_layout(graph)
    rest_nodes = path[1:-1]
    rest_nodes.remove(v0)
    nx.draw_networkx_nodes(graph, pos, nodelist=[v0], node_color='y')
    nx.draw_networkx_nodes(graph, pos, nodelist=[path[0]], node_color='b')
    nx.draw_networkx_nodes(graph, pos, nodelist=[path[-1]], node_color='r')
    nx.draw_networkx_nodes(graph, pos, nodelist=rest_nodes, node_color='w')
    nx.draw_networkx_edges(graph, pos, edgelist=edefault, width=1, alpha=0.1, arrows=True)
    nx.draw_networkx_edges(graph, pos, edgelist=epath, width=1, edge_color='b',arrows=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(graph, pos)
    plt.axis('off')
    plt.show()

    return True
