import heapq
def solution(operations) :
    answer = []
    maxheap = []
    minheap = []
    for i in range(len(operations)) :
        operator, number = operations[i].split(" ")
        num = int(number)
        if operator == "I" :
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, (-num, num))
        elif operator == "D" :
            if num == 1 :
                if(len(maxheap) != 0) :
                    max = heapq.heappop(maxheap)[1]
                    minheap.remove(max)
            elif num == -1 :
                if(len(minheap) != 0) :
                    min = heapq.heappop(minheap)
                    maxheap.remove((-min, min))
    if len(minheap) == 0 :
        answer.append(0)
        answer.append(0)
    else : 
        answer.append(heapq.heappop(maxheap)[1])
        answer.append(heapq.heappop(minheap))
    return answer

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))