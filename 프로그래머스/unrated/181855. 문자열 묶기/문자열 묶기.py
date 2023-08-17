def solution(strArr):
    answer = [0]*31
    for x in strArr:
        answer[len(x)] += 1
    return max(answer)