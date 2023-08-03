def solution(a, d, included):
    answer = []
    num = a
    result = 0
    for i in range(len(included)):
        answer.append(num)
        num = num + d
    for number, boo in zip(answer, included):
        if boo == True:
            result += number
    return result