def solution(n, computers):
    answer = 0
    check = [False] * n
    def dfs(computers, i, check) :
        for j in range(0, len(computers[i])) :
            if (computers[i][j] == 1 and check[j] == False) :
                check[j] = True
                dfs(computers, j, check) 
    for i in range(0, len(computers)) :
        if check[i] == False :
            answer += 1
            check[i] = True
            dfs(computers, i, check)

    return answer



n= 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))