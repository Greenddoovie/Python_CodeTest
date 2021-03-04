def solution(array, commands) :
    answer = []
    for i in range(len(commands)) :
        command = commands[i];
        start = command[0]-1
        end = command[1]
        kth = command[2]

        imsi = array[start:end]
        imsi.sort()
        answer.append(imsi[kth-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
