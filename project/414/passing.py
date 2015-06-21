import sys
from graph import Graph
from dijkstra import dijkstra, shortest
from utils import read_csv
from console import print_graph, print_path, print_instructions
import networkx as nx
import matplotlib.pylab as plt


def create_graph(vertices, edges):
    g = Graph()

    for vertex in vertices:
        g.add_vertex(vertex)

    for edge in edges:
        g.add_edge(edge['from'], edge['to'], edge['cost'])

    return g


def shortest_path(g, a, b):
    dijkstra(g, g.get_vertex(a))

    target = g.get_vertex(b)
    path = [target.get_id()]
    shortest(target, path)

    g.reset()

    return path


def get_path_passing_through_v0(paths_to_v0, v0_to_vertices, frm, to):
    path = []
    path.extend(v0_to_vertices[to])
    path.extend(paths_to_v0[frm][1:])

    return path


def compute_all_paths(g, vertices, v0):
    paths_to_v0 = {}
    v0_to_vertices = {}

    for vertex in vertices:
        paths_to_v0[vertex] = shortest_path(g, vertex, v0)
        v0_to_vertices[vertex] = shortest_path(g, v0, vertex)

    return [paths_to_v0, v0_to_vertices]


def find_edge(edges, frm, to):
    for edge in edges:
        if edge['from'] == frm and edge['to'] == to:
            return edge
    return None


def show_path(path, vertices, edges):
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
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=edefault, width=1, arrows=True)
    nx.draw_networkx_edges(graph, pos, edgelist=epath, width=1, alpha=0.5, edge_color='b',arrows=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(graph, pos)
    plt.axis('off')
    plt.show()

    return True


def main(v0, frm, to):
    [vertices, edges] = read_csv('graph.csv')

    g = create_graph(vertices, edges)
    print_graph(g)

    [paths_to_v0, v0_to_vertices] = compute_all_paths(g, vertices, v0)

    path = get_path_passing_through_v0(paths_to_v0, v0_to_vertices, frm, to)
    print_path(path)

    show_path(path, vertices, edges)


if __name__ == '__main__':
    v0 = 'a'
    frm = 'd'
    to = 'c'

    if len(sys.argv) is 4:
        vo = int(sys.argv[1])
        frm = int(sys.argv[2])
        to = int(sys.argv[3])
    else:
        print_instructions()

    main(v0, frm, to)
