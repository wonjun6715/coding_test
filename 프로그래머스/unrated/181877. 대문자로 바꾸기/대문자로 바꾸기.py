def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i].islower():
            answer += myString[i].upper()
        else:
            answer += myString[i]
    return answer