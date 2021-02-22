def solution(phone_book) :
    answer= True
    book = {}
    phone_book.sort(key=len, reverse = True)
    for i in range(0,len(phone_book)) :
        book[i] = phone_book[i]
    
    for i in range(0, len(phone_book)) :
        num = book[i]
        for j in range(len(phone_book)-1, i, -1) :
            if (num.startswith(book[j])) is True :
                answer = False
                break;
    return answer


phone_book = ['119', '97674223', '1195524421']
print(solution(phone_book))