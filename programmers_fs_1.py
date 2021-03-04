def solution(numbers, target):
    answer = 0


    def dfs(num, numbers, index, target) :
         
        if(index == len(numbers)-1) :
            if(num == target) :
                return 1
            else :
                return 0
        index += 1
        result = 0
        result += dfs(num  + numbers[index], numbers, index, target)
        result += dfs(num - numbers[index], numbers, index, target)
        return result
        
    answer = dfs(-numbers[0], numbers, 0, target) + dfs(numbers[0], numbers, 0, target) 

    return answer

numbers = [1, 1, 1, 1, 1]
target= 3
print(solution(numbers, target))