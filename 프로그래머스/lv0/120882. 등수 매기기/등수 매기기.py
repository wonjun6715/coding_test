def solution(score):
    result = []
    answer = [sum(x) for x in score] 
    for i in range(len(answer)):
        rank = 1
        for j in range(len(answer)):
            if answer[i] < answer[j]:
                rank += 1
        result.append(rank)    
    
    return result