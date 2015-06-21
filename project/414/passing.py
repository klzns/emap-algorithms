from graph import Graph
from dijkstra import dijkstra, shortest
from utils import read_csv



if __name__ == '__main__':
    [vertices, edges] = read_csv('graph.csv')

    g = Graph()

    for vertex in vertices:
        g.add_vertex(vertex)

    for edge in edges:
        g.add_edge(edge['from'], edge['to'], edge['cost'])

    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))


    dijkstra(g, g.get_vertex('a'))

    target = g.get_vertex('d')
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' %(path[::-1])
