def solution(s):
    answer = []
    answer.append(-1)
    for i in range(1, len(s)):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                answer.append(i - j)
                break
        else:
            answer.append(-1)
                
    return answer