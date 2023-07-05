def solution(s, n):
    answer = ''
    length = len(s)
    for i in range(length):
        if s[i] == ' ':
            answer += ' '
        elif ord(s[i]) >= ord('a') and ord(s[i]) + n > ord('z'):
            number = ord(s[i]) + n - 26
            answer += chr(number)
        elif ord(s[i]) <= ord('Z') and ord(s[i]) + n > ord('Z'):
            number = ord(s[i]) + n - 26
            answer += chr(number)
        else:
            answer += chr(ord(s[i]) + n)
    return answer