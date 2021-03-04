li = [6,8,4,2,7,9,134,86,42,75]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

li2 = [[1,2], (1,4), (1,1) ,(5,6) ,(7,8) ,(123,4), (543,653), (12,8576)]
print(li2)
li2.sort(key = lambda x : (-x[1], x[0]))
print(li2)
li2.sort(key = lambda x : (-x[1], -x[0]))
print(li2)
li2.sort(key = lambda x : x[1]+x[0])
print(li2)
li2.sort(key = lambda x : x[1]%x[0])
print(li2)

li3 = [(1,1) ,(1,2), (1,3), (2,1), (2,2), (3,1)]

print(li3)

squares = list(map(lambda x: x**2, range(10)))
print(squares)
li4 = [1,5]
li5 = [2,3]

li6 = [(x+y) for x,y in zip(li4,li5)]
print(li6)
li7 = []
for x, y in zip(li4,li5):
    li7.append(x+y)
print(li7)

l = [1,2,3,7,5,9,8]
import heapq
heap = []
for i in range(len(l)) :
    heapq.heappush(heap, l[i])
print(heap)