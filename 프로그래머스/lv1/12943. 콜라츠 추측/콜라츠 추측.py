def solution(num):
    answer = 0
    c = 0
    if num != 1:
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                answer += 1
            elif num % 2 == 1:
                num = num * 3 + 1
                answer += 1
            if answer == 500:
                return -1
    elif num == 1:
        answer = 0
    return answer