def solution(people, limit):
    answer = 0
    people.sort()
    while(people) :
        if(len(people) > 1) :
            first = people.pop()
            second = people[0]
            if( first == limit) :
                answer +=1
            elif(first + second <= limit) :
                people.remove(second)
                answer += 1
            else :
                answer += 1
        else :
            people.pop()
            answer += 1
        left = 0
        right = len(people)-1
        while(left <= right) :
            if(people[right] == limit) :
                answer +=1
                right -= 1
            elif (people[right] + people[left] <= limit) :
                answer += 1
                right -= 1
                left += 1
            else : 
                answer +=1
                right -= 1
        
        while(left < right) :
            if(len(people) >2 ) :
                if (people[right] + people[left] <= limit) :
                    left += 1
            answer +=1
            right -= 1
            
    return answer

people = [70,50,80,50]
limit = 100
print(solution(people,limit))