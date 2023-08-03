def solution(n):
    answer = 0
    cnt = 0
    for i in range(1, n + 1):
        answer = 0
        for j in range(1, n + 1):
            if i % j == 0:
                answer += 1
        if answer >= 3:
            cnt += 1
    return cnt