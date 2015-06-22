from utils import read_csv
import networkx as nx
import matplotlib.pylab as plt
from networkx.algorithms.flow import ford_fulkerson


def main():
    [x_cities, s_cities, v_cities, edges] = read_csv('cities.txt')

    graph = nx.DiGraph()

    graph.add_node('SOURCE')
    for vertex in x_cities:
        graph.add_node(vertex)
    for vertex in x_cities:
        graph.add_edge('SOURCE', vertex, capacity=1)

    graph.add_node('SINK')
    for vertex in s_cities:
        graph.add_node(vertex)
    for vertex in s_cities:
        graph.add_edge(vertex, 'SINK', capacity=1)

    for vertex in v_cities:
        graph.add_node(vertex)
    for edge in edges:
        graph.add_edge(edge['from'], edge['to'], capacity=1)

    flow_value, flow_dict = nx.maximum_flow(graph, 'SOURCE', 'SINK',
                                            flow_func=ford_fulkerson)

    temp_g = nx.DiGraph(flow_dict)
    edefault = []
    for (u, v, d) in temp_g.edges(data=True):
        if u != 'SOURCE' and v != 'SINK' and flow_dict[u][v] != 0:
            edefault.append((u, v))

    labels = {}
    all_cities = []
    all_cities.extend(s_cities)
    all_cities.extend(x_cities)
    all_cities.extend(v_cities)
    for vertex in all_cities:
        labels[vertex] = vertex

    G = nx.DiGraph(flow_dict)
    pos = nx.circular_layout(graph)
    nx.draw_networkx_edges(graph, pos, edgelist=edefault)
    nx.draw_networkx_nodes(graph, pos, nodelist=x_cities, node_color='r')
    nx.draw_networkx_nodes(graph, pos, nodelist=s_cities, node_color='b')
    nx.draw_networkx_nodes(graph, pos, nodelist=v_cities, node_color='y')
    nx.draw_networkx_labels(graph, pos, labels=labels)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
