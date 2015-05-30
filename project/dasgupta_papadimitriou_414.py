from collections import deque

graph = {
    'A': [
        {
            'node': 'B',
            'cost': 2,
        },
        {
            'node': 'C',
            'cost': 1
        }
    ],
    'B': [
        {
            'node': 'C',
            'cost': 3
        }
    ],
    'C': [
        {
            'node': 'D',
            'cost': 2
        }
    ],
    'D': [
        {
            'node': 'A',
            'cost': 3
        }
    ]
}

def revert_graph(graph, node):
    reverse_graph = {}
    for edge in graph[node]:
        if new_graph.has_key(edge.node):
            new_graph[edge.node].append({
                'node': node
                'cost': edge.cost
            })
        else:
            new_graph[edge.node] = [{
                'node': node,
                'cost': edge.cost
            }]
    return reverse_graph


def bfs(graph, start_node):
    path = {}
    path[start_node] = {
        'cost': 0,
        'nodes': []
    }

    queue = deque([start_node])

    while len(queue) > 0:
        current_node = queue.popleft()
        for node in graph[current_node]:
            if not path.has_key(node):
                queue.append(node)
                path[node] = {
                    'cost': (path[current_node]['cost'] + 1),
                    'nodes': [current_node]
                }
            else:
                path[node]['nodes'].append(current_node)

    return path


def shortest_paths_passing_through_v0(graph, v0):    
    if not graph.has_key(v0):
        print("Graph does not contain node v0")
        return None

    for node in graph[v0]:
        paths = bfs(graph, v0)

    print paths

if __name__ == '__main__':
    shortest_paths_passing_through_v0(graph, 'A')
        