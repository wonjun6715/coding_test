def solution(score):
    answer = [sum(x) for x in score]
    result = []
    a = sorted(answer, reverse = True)  
    for i in answer:
        result.append(a.index(i) + 1)
    return result