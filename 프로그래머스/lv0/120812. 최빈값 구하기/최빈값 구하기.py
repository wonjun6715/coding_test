def solution(array):
    answer = [0] * 1000
    for i in range(len(array)):
        answer[array[i]] += 1
    a = max(answer)
    if answer.count(a) >= 2:
        return -1
    else:
        return answer.index(a)
    