from queue import Queue
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = Queue(maxsize=bridge_length)
    bridge_weight = 0
    for i in range(0,len(truck_weights)) :
        truck = truck_weights[i]
        print(truck)
        while(True) :
            if (q.qsize() == bridge_length) is True :
                bridge_weight -= q.get()
                print("truck out")
            if (q.qsize ==0) | ((bridge_weight+ truck) <= weight) is True :
                print("truck in")
                q.put(truck)
                answer += 1
                bridge_weight += truck
                break
            else :
                print("wait truck")
                q.put(0)
                answer += 1
    answer += bridge_length            
    return answer


bridge_length = 2
weight = 10
truck_Weights = (7,4,5,6)
print(solution(bridge_length, weight, truck_Weights))