def solution(number, k):
    answer = ''
    cntRemain = len(number) - k
    cntRemove = 0
    count = 1
    index = -1
    while(count < cntRemain+1) : 
        val = "0"
        for i in range(index+1, k+count) :
            if number[i] > val :
                index = i
                val = number[i]
                if(val == "9") :
                    break
        answer += val
        count+=1
        # if(cntRemove != k) :
        #     print(range(index, k+count))
        #     print("count : " + repr(count))
        #     newI = number[index+1 : k + count].index(max(number[index+1 : k+count]))
        #     answer += number[index+newI]
        #     index += newI+1
        #     count += 1
        #     for i in range(newI) :
        #         cntRemove += 1
        # elif(cntRemove == k) : 
        #     for i in range(index, len(number)) :
        #         answer += number[i]
        #         count+=1
    return answer




number = "1924"
k =	2
print(solution(number,k))