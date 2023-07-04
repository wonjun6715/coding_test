def solution(s):
    answer = ''   
    position = 0
    array = ''
    result = list(map(str,s.split()))
    for i in range(len(result)):
        for j in range(len(result[i])):
            if j % 2 == 0:
                answer += result[i][j].upper()
            elif j % 2 == 1:
                answer += result[i][j].lower()
    for i in range(len(s)):
        if s[i] == ' ':
            array += ' '
        elif s[i] != ' ':
            array += answer[position]
            position += 1                
    return array