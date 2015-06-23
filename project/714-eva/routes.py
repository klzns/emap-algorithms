from utils import read_csv, get_all_cities, show_graph
import networkx as nx
from networkx.algorithms.flow import ford_fulkerson


# Essa funcao ira criar um grafo com as cidades como vertices e as estradas
# como arestas. Esse grafo tera um diferencial, que sao os vertices
# "SOURCE" e "SINK". Precisamos criar esses vertices artificiais para podermos
# usar o algoritmo de Ford-Fulkerson.
def create_graph(x_cities, s_cities, v_cities, edges):
    graph = nx.DiGraph()

    # Concatenamos todas as cidades em um unico array
    all_cities = get_all_cities(x_cities, s_cities, v_cities)

    # Adicionamos todas as cidades e arestas
    for vertex in all_cities:
        graph.add_node(vertex)
    for edge in edges:
        graph.add_edge(edge['from'], edge['to'], capacity=1)

    # Adicionamos um no como fonte para que possamos usar o algoritmo de Ford-Fulkerson
    graph.add_node('SOURCE')
    # Ligamos esse no a todos os vertices de cidades populadas (grupo X)
    for vertex in x_cities:
        graph.add_edge('SOURCE', vertex, capacity=1)

    # Adicionamos um no como sumidouro para que possamos usar o algoritmo de Ford-Fulkerson
    graph.add_node('SINK')
    # Ligamos esse no a todos os vertices de cidades seguras (grupo S)
    for vertex in s_cities:
        graph.add_edge(vertex, 'SINK', capacity=1)

    return graph


# Pega as arestas que foram usadas como caminho pelo Ford-Fulkerson
def get_path(flow_dict):
    edefault = []

    for city in flow_dict:
        for destination in flow_dict[city]:
            # Ignoramos as que tem relacao com os nos fonte e sumidouro
            # Pegamos aquelas que possuem valor diferente de zero, ou seja,
            # que sua capacidade esta sendo usada
            if (flow_dict[city][destination] != 0 and
               city != 'SOURCE' and destination != 'SINK'):
                edefault.append((city, destination))

    return edefault


def main():
    # Lemos o grafo de um arquivo
    [x_cities, s_cities, v_cities, edges] = read_csv('cities.txt')

    # Criamos o grafo com os vertices "SOURCE" e "SINK"
    graph = create_graph(x_cities, s_cities, v_cities, edges)

    # Chamamos o algoritmo de Ford-Fulkerson para o grafo
    flow_value, flow_dict = nx.maximum_flow(graph, 'SOURCE', 'SINK',
                                            flow_func=ford_fulkerson)

    # Pegamos apenas as arestas que foram que foram usadas pelo algoritmo
    edges_path = get_path(flow_dict)

    # Exibimos o grafo com o resultado
    show_graph(flow_dict, x_cities, s_cities, v_cities, edges_path)


if __name__ == '__main__':
    main()
