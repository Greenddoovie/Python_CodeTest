def solution(genres, plays):
    answer = []
    gp = {}
    for i in range(0, len(genres)) :
        if (genres[i] in gp) is True :
            gp[genres[i]] += plays[i]
        else :
            gp[genres[i]] = plays[i]

    pg = {}        
    tp = []
    for key, val in gp.items() :
        pg[val] = key
        tp.append(val)

    tp.sort(reverse = True)
    genre = []
    for i in tp :
        genre.append(pg[i])

    for g in genre :
        imsi = []
        for i in range(0, len(genres)) :
            if (g == genres[i]) is True :
                imsi.append([plays[i], i])
        
        imsi.sort(key = lambda x : (-x[0], x[1]))
        print(imsi)
        print(len(imsi))
        if (len(imsi) > 1) is True :
            answer.append(imsi[0][1])
            answer.append(imsi[1][1])
        elif (len(imsi) == 1) is True :
            answer.append(imsi[0][1])
        

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
result = solution(genres, plays)
print(result)