def solution(x, n):
    answer = []
    if x == 0:
        return [0] * n
    for i in range(x, x * (n + 1), x):
        answer.append(i)
    return answer