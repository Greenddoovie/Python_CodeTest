def solution(numbers) :
    answer = ''
    numbers.sort(key = lambda x : (-x/ (10**( len(str(x)) -1)), len(str(x))))
    for number in numbers :
        answer += str(number)
    return answer

number = [6, 10, 2]
number2 = [3, 30, 34,5 , 9]
number3 = [1000,1000, 999,799,111, 997, 99,1,40,4]

print(solution(number3))
# print("abc"[0])
print(list(map  ( lambda x : x / (10**(len(str(x))-1)), number3)))
print(997%100%10)
print(9%1)