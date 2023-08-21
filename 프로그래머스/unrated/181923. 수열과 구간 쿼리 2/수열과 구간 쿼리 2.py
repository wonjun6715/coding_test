def solution(arr, queries):
    answer = []
    result = []
    for s, e, k in queries:
        for i in range(len(arr)):
            if i >= s and i <= e:
                if arr[i] > k:
                    answer.append(arr[i])
        if answer:
            result.append(min(answer))
            answer.clear()
        else:
            result.append(-1)
    return result