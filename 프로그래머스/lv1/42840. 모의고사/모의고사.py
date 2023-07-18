def solution(answers):
    answer = []
    result = []
    pe1 = [1, 2, 3, 4, 5]
    pe2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pe3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    i = 0
    j = 0
    while True:
        if pe1[i] == answers[j]:
            cnt1 += 1
        i += 1
        j += 1
        if i == len(pe1):
            i = 0
        if j == len(answers):
            break
    i = 0
    j = 0
    while True:
        if pe2[i] == answers[j]:
            cnt2 += 1
        i += 1
        j += 1
        if i == len(pe2):
            i = 0
        if j == len(answers):
            break
    i = 0
    j = 0
    while True:
        if pe3[i] == answers[j]:
            cnt3 += 1
        i += 1
        j += 1
        if i == len(pe3):
            i = 0
        if j == len(answers):
            break
            
    answer = [cnt1, cnt2, cnt3]
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i + 1)
    return result
    
        
           