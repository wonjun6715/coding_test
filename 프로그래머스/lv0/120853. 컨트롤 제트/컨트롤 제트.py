def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False
def solution(s):
    answer = s.split()
    result = 0
    tmp = 0
    for i in range(len(answer)):        
        if is_digit(answer[i]):
            answer[i] = int(answer[i])
            result += answer[i]
            tmp = answer[i]
        else:
            result -= tmp
    return result