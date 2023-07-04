def solution(N, stages):
    answer = []
    index = []
    
    length = len(stages)
    for i in range(1, N + 1):
        if stages.count(i) == 0:
            answer.append(0)
        else:
            answer.append(stages.count(i) / length)
            length = length - stages.count(i)
            
    for i in range(N):
        index.append(answer.index(max(answer)) + 1)
        answer[answer.index(max(answer))] = -1
        
    return index