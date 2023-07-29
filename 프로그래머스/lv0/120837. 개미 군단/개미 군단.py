def solution(hp):
    answer = 0
    cnt = 0
    while True:
        while True:
            answer += 5
            cnt += 1
            if answer > hp:
                answer -= 5
                cnt -= 1
                break
        while True:
            answer += 3
            cnt += 1
            if answer > hp:
                answer -= 3
                cnt -= 1
                break
        while True:
            answer += 1
            cnt += 1
            if answer > hp:
                answer -= 1
                cnt -= 1
                break
        break
            
    return cnt