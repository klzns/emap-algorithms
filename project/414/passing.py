import sys
from graph import Graph
from dijkstra import dijkstra, shortest
from utils import read_csv, show_path
from console import print_graph, print_path, print_instructions


def create_graph(vertices, edges):
    g = Graph()

    for vertex in vertices:
        g.add_vertex(vertex)

    for edge in edges:
        g.add_edge(edge['from'], edge['to'], edge['cost'])

    return g


def shortest_path(g, a, b):
    # Computamos os menores caminhos com Dijkstra
    dijkstra(g, g.get_vertex(a))

    # Atribuimos o destino
    destination = g.get_vertex(b)
    path = [destination.get_id()]
    # Pegamos o caminho percorrido entre o vertice de origem ao destino
    shortest(destination, path)

    # Limpamos as variaveis e distancias calculadas pelo Dijkstra
    g.reset()

    return path


def get_path_passing_through_v0(paths_to_v0, v0_to_vertices, frm, to):
    path = []

    # O caminho total eh a juncao do caminho do vertice origem ate v0
    # junto com o caminho de v0 ate o vertice destino
    path.extend(v0_to_vertices[to])
    path.extend(paths_to_v0[frm][1:])

    return path


def compute_all_paths(g, vertices, v0):
    paths_to_v0 = {}
    v0_to_vertices = {}

    for vertex in vertices:
        # Computamos os caminhos do vertice ate v0
        paths_to_v0[vertex] = shortest_path(g, vertex, v0)
        # Computamos os caminhos de v0 ate o vertice
        v0_to_vertices[vertex] = shortest_path(g, v0, vertex)

    return [paths_to_v0, v0_to_vertices]


def main(v0, frm, to):
    [vertices, edges] = read_csv('graph.csv')

    g = create_graph(vertices, edges)
    print_graph(g)

    # Computamos todos os caminhos de e para v0
    [paths_to_v0, v0_to_vertices] = compute_all_paths(g, vertices, v0)

    # Pegamos o caminho de "frm" ate "to" passando por v0
    path = get_path_passing_through_v0(paths_to_v0, v0_to_vertices, frm, to)
    print_path(path)

    # Exibimos uma visualizacao grafica
    show_path(path, vertices, edges, v0)


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
