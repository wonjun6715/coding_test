def solution(n):
    answer = 0
    result = ''
    while n > 0:
        n, mod = divmod(n, 3)
        result += str(mod)
    result = result[::-1]
    for i in range(len(result)):
        answer = answer + (int(result[i]) * (3**i))
    return answer