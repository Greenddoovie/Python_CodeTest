import heapq
li = [[1,3], [2,4], [1,2], [2,7], [3,8], [3,6]]
heap = []
for i in range(len(li)) :
    heapq.heappush(heap, li[i])
print(heap)
for i in range(len(heap)) :
    print(heapq.heappop(heap))

li2 = [1,2,3,4,5,6,7]
heapq._heapify_max(li2)
print(heap[0])
for i in range(len(li2)) :
    print(heapq._heappop_max(li2))