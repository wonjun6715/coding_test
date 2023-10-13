import math
def solution(answers):
    answer = []
    pe1 = [1,2,3,4,5]
    pe2 = [2,1,2,3,2,4,2,5]
    pe3 = [3,3,1,1,2,2,4,4,5,5]
    ps1 = 0
    ps2 = 0
    ps3 = 0
    for i in range(len(answers)):
        if answers[i] == pe1[i % len(pe1)]:
            ps1 += 1
        if answers[i] == pe2[i % len(pe2)]:
            ps2 += 1
        if answers[i] == pe3[i % len(pe3)]:
            ps3 += 1
    answer = [ps1, ps2, ps3]
    result = []
    max_score = max(answer)
    for i in range(3):
        if max_score == answer[i]:
            result.append(i + 1)
    return result