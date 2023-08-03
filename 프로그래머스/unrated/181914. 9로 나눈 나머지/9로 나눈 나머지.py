def solution(number):
    answer = 0
    for i in number:
        answer += int(i)
    result = answer % 9
    return result