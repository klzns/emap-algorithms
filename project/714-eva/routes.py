from utils import read_csv
import networkx as nx
import matplotlib.pylab as plt
from networkx.algorithms.flow import ford_fulkerson


def main():
    [x_cities, s_cities, v_cities, edges] = read_csv('cities.txt')

    graph = nx.DiGraph()

    all_cities = []
    all_cities.extend(s_cities)
    all_cities.extend(x_cities)
    all_cities.extend(v_cities)

    print x_cities, v_cities
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

    # Chamamos o algoritmo de Ford-Fulkerson para o grafo
    flow_value, flow_dict = nx.maximum_flow(graph, 'SOURCE', 'SINK',
                                            flow_func=ford_fulkerson)

    # Pegamos apenas as arestas que foram que foram usadas pelo algoritmo
    edefault = []
    for city in flow_dict:
        for destination in flow_dict[city]:
            if (flow_dict[city][destination] != 0 and
               city != 'SOURCE' and destination != 'SINK'):
                edefault.append((city, destination))

    # Pegamos os nomes das cidades
    labels = {}
    for vertex in all_cities:
        labels[vertex] = vertex

    # Criamos um novo grafo
    G = nx.DiGraph(flow_dict)
    pos = nx.circular_layout(graph)
    # Inserimos todas as arestas
    nx.draw_networkx_edges(graph, pos, edgelist=edefault)
    # Inserimos as cidades populadas (grupo X) em vermelho
    nx.draw_networkx_nodes(graph, pos, nodelist=x_cities, node_color='r')
    # Inserimos as cidades seguras (grupo S) em azul
    nx.draw_networkx_nodes(graph, pos, nodelist=s_cities, node_color='b')
    # Inserimos as cidades restantes (grupo V) em amarelo
    nx.draw_networkx_nodes(graph, pos, nodelist=v_cities, node_color='y')
    # Inserimos os nomes das cidades
    nx.draw_networkx_labels(graph, pos, labels=labels)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
