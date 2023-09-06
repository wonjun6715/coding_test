# 1 2 3 1
def solution(ingredient):
    current_stack = []
    answer = 0
    for i in ingredient:
        current_stack.append(i)
        if current_stack[-4:] == [1, 2, 3, 1]:
            del current_stack[-4:]
            answer += 1
    
    return answer