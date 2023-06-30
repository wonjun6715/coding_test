def solution(s):
    answer = True
    cp = 0
    cy = 0
    for i in range(len(s)):
        if s[i] in 'Pp':
            cp+=1
        elif s[i] in 'Yy':
            cy+=1
    if cp == 0 and cy == 0:
        return True
    if cp == cy:
        return True
    else:
        return False