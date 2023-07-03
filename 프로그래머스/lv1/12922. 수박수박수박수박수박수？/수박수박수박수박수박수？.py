def solution(n):
    answer = ''
    for i in range(n):
        if (i + 1) % 2 == 1:
            answer += '수'
        elif (i + 1) % 2 == 0:
            answer += '박'
    return answer