def solution(n, results):
    answer = 0
    
    playerWin = []
    playerLose = []
    for i in range(0, n+1) :
        playerWin.append([])
        playerLose.append([])
    
    for i in range(0, len(results)) :
        playerWin[results[i][0]].append(results[i][1])
        playerLose[results[i][1]].append(results[i][0])

    for i in range(1, len(playerWin)) :
        loser = playerWin[i]
        if loser :
            for j in range(0, len(loser)) :
                loser2 = playerWin[loser[j]]
                if loser2 :
                    for l in range(0, len(loser2)) :
                        if loser2[l] in loser :
                            continue
                        else :
                            loser.append(loser2[l])
    
    for i in range(1, len(playerLose)) :
        winner = playerLose[i] 
        if winner :
            for j in range(0, len(winner)) :
                winner2 = playerLose[winner[j]]
                if winner2 :
                    for l in range(0, len(winner2)) :
                        if winner2[l] in winner :
                            continue
                        else :
                            winner.append(winner2[l])
                    
    for i in range(1, len(playerWin)) :
        match = len(playerWin[i]) + len(playerLose[i])
        if ( match == n-1) :
            answer +=1

    return answer

n =5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))