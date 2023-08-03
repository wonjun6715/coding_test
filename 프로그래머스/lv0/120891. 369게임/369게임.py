def solution(order):
    answer = 0
    result = str(order)
    for i in range(3,10,3):
        answer += result.count(str(i))
    return answer