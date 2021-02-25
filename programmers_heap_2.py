import heapq

def solution(jobs):
    answer = 0
    # heap에 한 번에 다 넣으면 안되므로 현재 시간보다 작거나 같은 시간에 들어온 job들을 heap어 넣어준다
    # heap에서 처리는 처리시간이 빠른 순서대로 진행해야 가장 평균시간이 적게 걸리므로 job의 순서를 바꿔서 넣어준다
    # for문으로 jobs를 하나씩 넣어주는데 그 안에 while을 넣어서 돌린다
    heap = []
    time = 0
    usedI = 0
    i = 0
    jobs.sort(key = lambda x : x[0])
    while i < len(jobs) :
        if(usedI < len(jobs) and jobs[usedI][0] <= time) :
            heapq.heappush(heap, (jobs[usedI][1], jobs[usedI][0]))
            usedI += 1
        elif usedI < len(jobs) and len(heap) ==0 :
            time = jobs[usedI][0]
            heapq.heappush(heap, (jobs[usedI][1], jobs[usedI][0]))
            usedI += 1
        else : 
            job = heapq.heappop(heap)
            time += job[0]
            answer += time -job[1]
            i += 1

            # time 보다 큰 경우 혹은 처리해야하는게 있는경우
    answer = answer // len(jobs)
    return answer



# 다른 시간대에 들어온 요청들 중에서 같은 처리시간을 가지면 어떻게 될까?
#  0 4초
#  3초  5초
#  4초에 5초
# 4 + 6 + 10 = 20
# 4 + 5 + 11 = 20 --> 같다 결국 처리해야하는 순간에 처리 시간이 빠른 순서대로 넣어주면 된다
# 2차원 리스트를 heap하면? 0th index에 맞춰서 순서는 정해지나 1th index는 신경쓰지 않음
#  뒤늦게 들어온다면?

jobs = [[0, 3], [1, 9], [2, 6]]	
print(solution(jobs))