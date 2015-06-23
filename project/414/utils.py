import csv
import networkx as nx
import matplotlib.pylab as plt


def read_csv(filename):
    vertices = []
    edges = []

    # Le matriz de incidencia
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(spamreader):
            if i == 0:
                vertices = row
                continue
            edges.append(row)

    # Mapeia as arestas
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


# Procura a aresta que possui o no de inicio e fim providos
def find_edge(edges, frm, to):
    for edge in edges:
        if edge['from'] == frm and edge['to'] == to:
            return edge
    return None


# Exibe uma visualizacao grafica do resultado
def show_path(path, vertices, edges, v0):
    graph = nx.DiGraph()

    # Criamos o grafo no formato do Networkx
    for vertex in vertices:
        graph.add_node(vertex)

    # Adicionamos as arestas a informacao que ela faz parte do caminho
    edges = edges[:]
    for i, node in enumerate(path):
        if i > 0:
            edge = find_edge(edges, path[i-1], node)
            if edge is None:
                continue
            edge['path'] = True

    # Separamos as arestas que fazem parte do caminho das que nao fazem
    edefault = []
    epath = []
    for edge in edges:
        if 'path' not in edge:
            edge['path'] = False
            edefault.append((edge['from'], edge['to']))
        else:
            epath.append((edge['from'], edge['to']))

        # Adicionamos todas as arestas ao grafo
        graph.add_edge(edge['from'], edge['to'], weight=edge['cost'], cost=edge['path'])

    # Pegamos os pesos das arestas
    edge_labels = dict([((u, v, ), d['weight']) for (u, v, d) in graph.edges(data=True)])

    # Diferenciamos nos que nao sao destino, origem ou v0
    rest_nodes = path[1:-1]
    rest_nodes.remove(v0)

    pos = nx.circular_layout(graph)
    # Exibimos v0 como amarelo
    nx.draw_networkx_nodes(graph, pos, nodelist=[v0], node_color='y')
    # Exibimos no de origem como azul
    nx.draw_networkx_nodes(graph, pos, nodelist=[path[0]], node_color='b')
    # Exibimos no destino como vermelho
    nx.draw_networkx_nodes(graph, pos, nodelist=[path[-1]], node_color='r')
    # Todos os outros nos em branco
    nx.draw_networkx_nodes(graph, pos, nodelist=rest_nodes, node_color='w')
    # Arestas nao usadas pelo melhor caminho em cinza
    nx.draw_networkx_edges(graph, pos, edgelist=edefault, width=1, alpha=0.1, arrows=True)
    # Arestas usadas pelo melhor caminho em azul
    nx.draw_networkx_edges(graph, pos, edgelist=epath, width=1, edge_color='b',arrows=True)
    # Imprimimos o peso das arestas
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    # Imprimimos o nome dos nos
    nx.draw_networkx_labels(graph, pos)
    plt.axis('off')
    plt.show()

    return True
