def solution(n, times):
    answer = n * times[len(times) -1]
    times.sort()
    left = 1
    right = times[len(times)-1] * n
    while(left<=right) :
        people = 0
        mid = (left + right ) // 2
        for i in range(0, len(times)) :
            people += mid // times[i]
        if(people >= n ) :
            if (answer > mid ) :
                answer = mid
            right = mid -1;
        else :
            left = mid + 1
        

    return answer

n= 6
times =	[7, 10]
print(solution(n,times))