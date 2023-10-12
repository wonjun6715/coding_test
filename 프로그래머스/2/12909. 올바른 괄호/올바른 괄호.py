def solution(s):
    answer = True
    stack = []
    if s[0] == ')' or s[-1] == '(':
        return False
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True       
    return False