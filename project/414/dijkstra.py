import heapq
from console import print_dijkstra, print_update, print_not_updated


def shortest(v, path):
    # Pegamos o caminho fazendo o caminho inverso, do destino a origem
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start):
    print_dijkstra()
    # Define a distancia do no de inicio como zero
    start.set_distance(0)

    # Coloca o par de tupla na heap
    unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Retira o vertice com a menor distancia
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        # Para o proximo no connectado
        for next in current.connected:
            # Se estiver visitado, pula
            if next.visited:
                continue

            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print_update(current.get_id(), next.get_id(),
                             next.get_distance())
            else:
                print_not_updated(current.get_id(), next.get_id(),
                                  next.get_distance())

        # Reconstruimos a heap
        # Tiramos todos os items
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        # Colocamos todos os vertices nao visitados na heap
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
