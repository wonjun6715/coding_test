def solution(arr, k):
    answer = []
    result = []
    for i in arr:
        if not i in result:
            result.append(i)
    if len(result) > k:
        result = result[:k]
    else:
        for i in range(k - len(result)):
            result.append(-1)
    return result