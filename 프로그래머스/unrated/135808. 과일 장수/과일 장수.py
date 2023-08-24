def solution(k, m, score):
    answer = sorted(score, reverse=True)
    result = []
    price = 0
    for i in range(0, len(answer), m):
        if i >= len(answer):
            break
        result.append(answer[i:i+m])
    for i in range(len(result)):
        if len(result[i]) == m:
            price = price + (result[i][len(result[i]) - 1] * m)
    return price