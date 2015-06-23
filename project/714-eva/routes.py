from utils import read_csv, get_all_cities
import networkx as nx
import matplotlib.pylab as plt
from networkx.algorithms.flow import ford_fulkerson


def create_graph(x_cities, s_cities, v_cities, edges):
    graph = nx.DiGraph()

    all_cities = get_all_cities(x_cities, s_cities, v_cities)

    # Adicionamos todas as cidades e arestas
    for vertex in all_cities:
        graph.add_node(vertex)
    for edge in edges:
        graph.add_edge(edge['from'], edge['to'], capacity=1)

    # Adicionamos um no fonte para que possamos usar o algoritmo de Network Flow
    graph.add_node('SOURCE')
    # Ligamos esse no a todos os vertices de cidades populadas (grupo X)
    for vertex in x_cities:
        graph.add_edge('SOURCE', vertex, capacity=1)

    # Adicionamos um no sumidouro para que possamos usar o algoritmo de Network Flow
    graph.add_node('SINK')
    # Ligamos esse no a todos os vertices de cidades seguras (grupo S)
    for vertex in s_cities:
        graph.add_edge(vertex, 'SINK', capacity=1)

    return graph


def get_path(flow_dict):
    edefault = []

    for city in flow_dict:
        for destination in flow_dict[city]:
            if (flow_dict[city][destination] != 0 and
               city != 'SOURCE' and destination != 'SINK'):
                edefault.append((city, destination))

    return edefault


def get_city_names(x_cities, s_cities, v_cities):
    labels = {}

    all_cities = get_all_cities(s_cities, x_cities, v_cities)

    for vertex in all_cities:
        labels[vertex] = vertex

    return labels


def show_graph(flow_dict, x_cities, s_cities, v_cities, edges):
    # Criamos um novo grafo
    G = nx.DiGraph(flow_dict)
    pos = nx.circular_layout(G)

    # Inserimos todas as arestas
    nx.draw_networkx_edges(G, pos, edgelist=edges)

    # Inserimos as cidades populadas (grupo X) em vermelho
    nx.draw_networkx_nodes(G, pos, nodelist=x_cities, node_color='r')

    # Inserimos as cidades seguras (grupo S) em azul
    nx.draw_networkx_nodes(G, pos, nodelist=s_cities, node_color='b')

    # Inserimos as cidades restantes (grupo V) em amarelo
    nx.draw_networkx_nodes(G, pos, nodelist=v_cities, node_color='y')

    # Inserimos os nomes das cidades
    labels = get_city_names(x_cities, s_cities, v_cities)
    nx.draw_networkx_labels(G, pos, labels=labels)

    plt.axis('off')
    plt.show()


def main():
    [x_cities, s_cities, v_cities, edges] = read_csv('cities.txt')

    # Criamos o grafo
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
