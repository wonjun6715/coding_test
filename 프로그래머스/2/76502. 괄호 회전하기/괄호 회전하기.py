def bracket(s):
    stack = []
    for i in s:
        if len(stack) == 0: 
            stack.append(i)      
        else:
            if i == ']' and stack[-1] == '[': 
                stack.pop()
            elif i == ')' and stack[-1] == '(': 
                stack.pop()
            elif i == '}' and stack[-1] == '{': 
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        return True
    else:
        return False

def solution(s):
    cnt = 0
    for i in range(len(s)):
        if bracket(s) == True:
            cnt += 1
        s = s[1:] + s[0]
    return cnt