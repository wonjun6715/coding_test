def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        # 안잃어버린 학생
        if i not in lost:
            answer += 1
        # 잃어버렸지만 여분이 있는 학생
        elif i in lost and i in reserve:
            answer += 1
            lost.remove(i)
            reserve.remove(i)
        # 잃어버렸지만 앞 학생이 여분이 있는 경우
    for i in range(1, n + 1):
        if i in lost and i - 1 in reserve:
            answer += 1
            lost.remove(i)
            reserve.remove(i - 1)
        # 잃어버렸지만 뒤 학생이 여분이 있는 경우
        if i in lost and i + 1 in reserve:
            answer += 1
            lost.remove(i)
            reserve.remove(i + 1)
    return answer
