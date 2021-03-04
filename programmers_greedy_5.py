def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : (x[2], x[0]))
    
    connect = []
    for i in range(n):
        connect.append(i)

    def findParent(land, connect) :
        if (connect[land] == land) :
            return connect[land]
        else : 
            return findParent(connect[land], connect)

    for i in range(0, len(costs)) :
        first = findParent(costs[i][0], connect)
        second = findParent(costs[i][1], connect)
        if(first != second) :
            connect[second] = first
            answer+= costs[i][2]
        

    print(connect)
    return answer

def solution2(n, costs):
    answer = 0
    costs.sort(key = lambda x : (x[2], x[0]))
    
    connect = []
    for i in range(n):
        connect.append(i)

    def findParent(land, connect) :
        if (connect[land] == land) :
            return connect[land]
        else : 
            return findParent(connect[land], connect)

    for i in range(0, len(costs)) :
        first = findParent(costs[i][0], connect)
        second = findParent(costs[i][1], connect)
        if(first != second) :
            connect[costs[i][1]] = first
            answer+= costs[i][2]
        

    print(connect)
    return answer


n = 5
costs = [[0,1,1],[3,4,1],[1,2,2],[2,3,4]]
print(solution(n, costs))
print(solution2(n, costs))