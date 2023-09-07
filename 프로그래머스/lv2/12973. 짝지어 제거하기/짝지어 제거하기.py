def solution(s):
    answer = -1
    tmp = []
    for x in s:
        tmp.append(x)
        if len(tmp) > 1 and tmp[-1] == tmp[-2]:
            tmp.pop()
            tmp.pop()
    
    if tmp:
        return 0
    else:
        return 1
        

    return tmp