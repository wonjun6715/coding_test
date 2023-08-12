def solution(myString, pat):
    answer = 0
    cnt = 0
    for i in range(len(myString) - len(pat) + 1):
        cnt = 0
        if myString[i] == pat[0]:
            for j in range(len(pat)):
                if myString[i + j] == pat[j]:
                    cnt += 1
            if cnt == len(pat):
                answer += 1
    return answer