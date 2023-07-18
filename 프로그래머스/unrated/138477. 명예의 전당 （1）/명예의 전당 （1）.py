def solution(k, score):
    answer = []
    result = []
    if k > len(score):
        result = [min(score[:i]) for i in range(1, len(score) + 1)]
        return result
    for i in range(k):
        answer.append(score[i])
        result.append(min(answer))
    answer.sort(reverse = True)
            
    for j in range(k, len(score)):
        if score[j] > answer[k - 1]:
            answer[k - 1] = score[j]
            answer.sort(reverse = True)
            result.append(min(answer))
        else:
            result.append(answer[k - 1])
    return result