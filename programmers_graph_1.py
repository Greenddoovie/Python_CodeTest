from collections import deque
def solution(n, edge):
    answer = 0
    distance = []
    graph = []
    for i in range(n+1) :
        graph.append([])
        distance.append(n+1)
    print(graph)
    edge.sort()
    print(edge)
    for i in range(0, len(edge)) :
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    print(graph)
    q = deque()
    distance[0] = 0
    distance[1] = 0
    q.append((1, 0))
    while q :
        now = q.popleft()
        vertex = graph[now[0]]
        for i in range(0, len(vertex)) :
            node = vertex[i]
            dis = now[1] + 1
            if(dis < distance[node]) :
                q.append((node, dis))
                distance[node] = dis
    print(distance)
    maxnum = max(distance)
    answer = distance.count(maxnum)
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n, edge))