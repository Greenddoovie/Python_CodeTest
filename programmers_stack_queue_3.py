def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while(len(progresses)>0) :
        count = 0
        while(progresses[len(progresses)-1] >= 100) :
            count += 1
            print("B pop : " + repr(len(progresses)))
            progresses.pop()
            print("A pop : " + repr(len(progresses)))
            if(len(progresses) == 0) is True:
                break
        if(count >0) is True : 
            answer.append(count)
        if(len(progresses) != 0) is True :
            while(progresses[len(progresses)-1] <100 ) :
                progresses = [(x+y) for (x,y) in zip(progresses, speeds)]
    return answer


progress = [93,30,55]
speeds = [1,30,5]
print(solution(progress, speeds))    

