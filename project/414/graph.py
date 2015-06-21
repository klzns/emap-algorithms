import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.connected = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_connection(self, vertex, weight=0):
        self.connected[vertex] = weight

    def get_connections(self):
        return self.connected.keys()

    def get_id(self):
        return self.id

    def get_weight(self, vertex):
        return self.connected[vertex]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' connected: ' + str([x.id for x in self.connected])


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_connection(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def reset(self):
        for vertex in self.vert_dict:
            self.vert_dict[vertex].set_distance(sys.maxint)
            self.vert_dict[vertex].previous = None
            self.vert_dict[vertex].visited = False
