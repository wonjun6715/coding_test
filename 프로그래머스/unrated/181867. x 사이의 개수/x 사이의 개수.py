def solution(myString):
    answer = []
    result = []
    answer = myString.split('x')
    for i in range(len(answer)):
        result.append(len(answer[i]))
    return result