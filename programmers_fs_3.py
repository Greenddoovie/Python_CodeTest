def solution(begin, target, words):
    answer = 51
    check = [False] * len(words)
    
    def possible(a, b) :
        count = 0
        for i in range(len(a)) :
            if(a[i] != b[i]) :
                count+=1
        if count == 1 :
            return True
        else :
            return False
    # 변할 수 있는지
    
    def bfs(word, target, words, check, count, answer) :
        if(word == target) :
            if(answer > count) :
                answer = count
            return answer
        for i in range(0, len(words)) :
            if(check[i] == False and possible(word, words[i]) == True) :
                check[i] = True
                result = bfs(words[i], target, words, check, count+1, answer)
                if( answer > result ) :
                    answer = result
                check[i] = False
        return answer
        

    for i in range(0, len(words)) :
        if (possible(begin, words[i])) :
            check[i] = True
            result = bfs(words[i], target, words, check, 1, answer)
            if (answer > result) :
                answer = result
            check[i] = False

    if answer == 51 :
        answer = 0

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))