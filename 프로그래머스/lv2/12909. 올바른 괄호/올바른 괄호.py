def solution(s):
    answer = True
    cnt = 0
    cnt2 = 0
    if s[0] == ')' or s[len(s) - 1] == '(':
        return False
    for i in range(len(s)):
        if cnt - cnt2 < 0:
            return False
        elif s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt2 += 1
    if cnt - cnt2 != 0:
        return False
    return True