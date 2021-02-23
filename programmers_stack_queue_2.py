def solution(prices):
    answer = []
    stack1 = list(prices)
    stack2 = []
    length = len(stack1)
    for i in range(0, length) :
        imsiStack = stack2.copy()
        price = stack1.pop()
        time = 0
        length2 = len(imsiStack)
        if length2 is 0 :
            answer.append(time)
            stack2.append(price)
        else :
            for j in range(0, length2) :
                comp = imsiStack.pop()
                time += 1
                if (price > comp ) is True :
                    answer.append(time)
                    stack2.append(price)
                    break
                elif( price <= comp) is True :
                    if (j == (length2-1)) is True :
                        answer.append(time)
                        stack2.append(price)
    answer.reverse()
    return answer

def solution2(prices) :
    answer = []
    for i in range(0, len(prices)-1) :
        price1 = prices[i]
        time = 1
        for j in range(i+1, len(prices)) :
            
            price2 = prices[j]
            if(price1 > price2) is True :
               answer.append(time)
               break
            else :
                if(j == (len(prices)-1) ) is True :
                    answer.append(time)
                else :  
                    time += 1 
    answer.append(0)
    return answer

prices = (1,2,3,2,3)
# print(solution(prices))
print(solution2(prices))