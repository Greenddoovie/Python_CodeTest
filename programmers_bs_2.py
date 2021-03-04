def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 0
    right = distance
    
    while ( left <= right) :
        mid = (left + right) // 2
        count = 0
        now = 0
        for i in range (0, len(rocks)) :
            rock = rocks[i]
            if (rock-now) >= mid :
                now = rock
            else :
                count += 1
        if (distance - now) < mid :
            count += 1
        if(count >n) :
            right = mid -1
        else :
            if(mid > answer) :
                answer = mid
            left = mid+1
        
     
    return answer


distance = 25
rocks =	[2, 14, 11, 21, 17]
n =	2
print(solution(distance, rocks, n))

