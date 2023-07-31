def solution(myString):
    answer = []
    result = []
    answer = myString.split('x')
    answer.sort()
    for i in answer:
        if i != "":
            result.append(i)
    return result