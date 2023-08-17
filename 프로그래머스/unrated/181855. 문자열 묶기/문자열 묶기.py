def solution(strArr):
    answer = []
    max = 0
    for i in range(len(strArr)):
        answer.append(len(strArr[i]))
    result = list(set(answer))
    for i in range(len(result)):
        if max < answer.count(result[i]):
            max = answer.count(result[i])
    return max