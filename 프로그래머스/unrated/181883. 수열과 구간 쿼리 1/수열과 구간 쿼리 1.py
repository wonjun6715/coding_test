def solution(arr, queries):
    answer = arr.copy()
    for query in queries:
        s, e = query[0], query[1]
        for i in range(s, e + 1):
            answer[i] += 1
    return answer