def solution(intStrs, k, s, l):
    answer = []
    for word in intStrs:
        result = word[s: s + l]
        result = int(result)
        if result > k:
            answer.append(result)
    return answer