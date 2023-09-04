def solution(s):
    cnt1 = 0
    cnt2 = 0
    answer = 0
    for i in s:
        if cnt1 == cnt2:
            answer += 1
            k = i
        if i == k:
            cnt1 += 1
        else:
            cnt2 += 1
    return answer