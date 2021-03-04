from collections import deque
import copy
def solution(tickets):
    answer = []
    
    for i in range(0, len(tickets)) :
        if(tickets[i][0] == "ICN") :
            start = tickets[i][0]
            land = tickets[i][1]
            routes = start + "," + land + ","
            check = [False] * len(tickets)
            check[i] = True
            q = deque()
            q.append((routes, 1, check))
            while q :
                now = q.popleft()
                lands = now[0]
                visited= now[2]
                if now[1] == len(tickets) :
                    route = lands.split(",")
                    route.pop()
                    answer.append(route)
                elif now[1] > len(tickets) :
                    continue
                lastCity = lands[len(lands)-4 : len(lands)-1]
                for j in range(0, len(tickets)) :
                    
                    if tickets[j][0] == lastCity:
                        if visited[j] == False :
                            visited2 = copy.deepcopy(visited)
                            visited2[j] = True 
                            lands += tickets[j][1] + ","
                            q.append((lands, now[1]+1, visited2))
                            lands = lands[:len(lands)-4]

    answer.sort()
    return answer[0]



tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(tickets))