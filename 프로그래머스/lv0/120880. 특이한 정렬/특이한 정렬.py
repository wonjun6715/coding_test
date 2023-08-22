def solution(numlist, n):
    answer = []
    result = []
    for i in numlist:
        answer.append(abs(n - i))
    a = list(zip(numlist, answer))
    tmp = sorted(a, key=lambda x: (x[1], -x[0]))
    for a,b in tmp:
        result.append(a)
    return result