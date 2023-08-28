def solution(n, lost, reserve):
    answer = [0] * (n+1)
    cnt = 0
    for i in range(1, len(answer)):
        if i in lost and i in reserve:
            continue
        elif i in reserve:
            answer[i] += 1
        elif i in lost:
            answer[i] -= 1

    for i in range(1, len(answer)):
        if i == 1:  # 가장 왼쪽 학생일 때
            if answer[i] == -1 and answer[i + 1] == 1:
                answer[i] += 1
                answer[i + 1] -= 1
        elif i == n:  # 가장 오른쪽 학생일 때
            if answer[i] == -1 and answer[i - 1] == 1:
                answer[i] += 1
                answer[i - 1] -= 1
        else:
            if answer[i] == -1:
                if answer[i - 1] == 1:
                    answer[i] += 1
                    answer[i - 1] -= 1
                elif answer[i + 1] == 1:
                    answer[i] += 1
                    answer[i + 1] -= 1

    for i in range(1, len(answer)):
        if answer[i] >= 0:
            cnt += 1
    return cnt