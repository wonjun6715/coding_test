def solution(l, r):
    
    answer = []
    for i in range(l, r+1):
        ch = str(i)
        if i % 5 != 0:
            continue
        for i in range(len(ch)):
            if '5' not in ch[i] and '0' not in ch[i]:
                break
        else:
            answer.append(int(ch))
    if answer:
        return answer
    else:
        return [-1]