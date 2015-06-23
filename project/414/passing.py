import sys
from graph import Graph
from dijkstra import dijkstra, shortest
from utils import read_csv, show_path
from console import print_graph, print_path, print_instructions, print_shortest_path, print_all_paths


def create_graph(vertices, edges):
    g = Graph()

    for vertex in vertices:
        g.add_vertex(vertex)

    for edge in edges:
        g.add_edge(edge['from'], edge['to'], edge['cost'])

    return g


def compute_all_shortest_paths(g, vertices):
    shortest_paths = {}

    for a in vertices:
        shortest_paths[a] = {}
        dijkstra(g, g.get_vertex(a))
        for b in vertices:
            destination = g.get_vertex(b)
            path = [destination.get_id()]
            shortest(destination, path)
            shortest_paths[a][b] = path
        g.reset()

    return shortest_paths


def get_path_passing_through_v0(shortest_paths, v0, frm, to):
    path = []

    # O caminho total eh a juncao do caminho do vertice origem ate v0
    # junto com o caminho de v0 ate o vertice destino.

    # Neste caso, pegamos primeiro de v0 ate o destino e depois
    # da origem ate v0, pois o caminho eh recuperado de tras para frente
    path.extend(shortest_paths[v0][to])
    path.extend(shortest_paths[frm][v0][1:])

    # Invertemos o caminho, ja que ele eh gerado de tras para frente
    return path[::-1]


def all_paths(shortest_paths, v0):
    print_all_paths()
    for frm in shortest_paths:
        for to in shortest_paths[frm]:
            path = get_path_passing_through_v0(shortest_paths, v0, frm, to)
            print_path(path)


def main(v0, frm, to):
    # Lemos a matriz de adjacencia que gera o grafo
    [vertices, edges] = read_csv('graph.csv')

    g = create_graph(vertices, edges)
    print_graph(g)

    # Computamos todos os melhores caminhos
    shortest_paths = compute_all_shortest_paths(g, vertices)

    # Imprimimos todos os menores caminhos passando por v0
    all_paths(shortest_paths, v0)

    # Pegamos o caminho de "frm" ate "to" passando por v0
    path = get_path_passing_through_v0(shortest_paths, v0, frm, to)
    print_shortest_path(v0, frm, to)
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
