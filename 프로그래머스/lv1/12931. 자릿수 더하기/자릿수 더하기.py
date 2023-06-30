def solution(n):
    answer = str(n)
    sum = 0
    for i in range(len(answer)):
        sum += int(answer[i])
    return sum