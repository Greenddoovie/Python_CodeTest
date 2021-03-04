graph = {
    'A' : {'B' : 6, 'D' : 10 , 'E' : 15},
    'B' : {'C' : 2, 'F' : 11},
    'C' : {'B' : 5, 'D' : 7, 'F' : 7, 'E' : 21},
    'D' : {'A' : 1, 'F' : 24, 'E' : 5},
    'E' : {'A' : 9, 'D' : 3, 'F' : 8},
    'F' : {'C' : 99}
}

import heapq

def dijkstra(graph, start) :
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue :
        current_distance, current_destination = heapq.heappop(queue)
        if(distances[current_destination] < current_distance) :
            continue

        for new_destinaiton, new_distance in graph[current_destination].items() :
            distance = current_distance + new_distance
            if(distance < distances[new_destinaiton]) :
                distances[new_destinaiton] = distance
                heapq.heappush(queue,[distances[new_destinaiton], new_destinaiton])
    return distances

print(dijkstra(graph, 'A'))
