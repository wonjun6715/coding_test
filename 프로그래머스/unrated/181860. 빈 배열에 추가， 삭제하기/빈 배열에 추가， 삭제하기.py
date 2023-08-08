def solution(arr, flag):
    answer = []
    for a, b in zip(arr, flag):
        if b == True:
            for i in range((a*2)):
                answer.append(a)
        else:
            for j in range(a):
                del answer[-1]
                
    return answer