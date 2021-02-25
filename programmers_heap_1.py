import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)
    
    while(scoville[0]<K) :
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        answer += 1
        heapq.heappush(scoville, new)
        
        if (len(scoville)  == 1) :
            if(scoville[0] < K) :
                answer = -1
                break
            
    return answer

scoville = [1, 2, 3]
K = 11
print(solution(scoville, K))

# heapq.heapify ==> 원래의 리스트를 힙으로 만듬, tuple은 힙으로 만들 수 없음, 순서는 그대로
