def solution(price, money, count):
    answer = -1
    result = 0
    for i in range(1, count + 1):
        result = result + (price * i)
    if money - result < 0:
        answer = (money - result) * -1
    else:
        return 0
    return answer