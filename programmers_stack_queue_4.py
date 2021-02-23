from queue import Queue
def solution(priorities, location):
    answer = 0
    count = 0
    li = [(x,y) for x,y in zip(priorities,  [ x for x in range(len(priorities))])]
    q = Queue()
    for i in li :
        q.put(i)
    
    while(q.qsize()>0 | answer == 0) :
        max = 0
        
        for i in range(0,q.qsize()) :
            now = q.get()
            if now[0] >max :
                max = now[0]
            q.put(now)
        for i in range(q.qsize()) :
            now = q.get()
            if now[0] == max :
                count += 1
                i-=1
                if now[1] == location :
                    answer = count
                break
            else : 
                q.put(now)
                
    
    return answer


priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))