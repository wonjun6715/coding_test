def solution(arr):
    answer = []
    minimum = min(arr)
    minidx = 0
    if len(arr) == 1:
        answer.append(-1)
        return answer
    for i in range(len(arr)):
        if minimum != arr[i]:
            answer.append(arr[i])
    return answer