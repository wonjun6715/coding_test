def solution(s):
    answer = ''
    answer += s[0].upper()
    for i in range(1, len(s)):        
        if s[i].islower() and s[i - 1] == ' ':
            answer += s[i].upper()
        elif s[i].isupper() and s[i - 1] == ' ':
            answer += s[i]
        else: 
            answer += s[i].lower()
    return answer