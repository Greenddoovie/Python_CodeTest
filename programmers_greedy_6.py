def solution(routes):
    answer = 1
    routes.sort(key = lambda x : (x[0], x[1]))
    e1 = routes[0][1]
    index = 1
    while(index < len(routes)) :
        s2, e2 = routes[index]
        index += 1

        if(e1 >= s2) :
            if(e1 >= e2) :
                e1 = e2
        elif(s2 > e1) :
            e1 = e2
            answer += 1
            print("b"+ repr(index))
        


    return answer


routes = 	[[-10, -5], [-5, 10], [0, 3], [3, 6], [9, 12]]
print(solution(routes))