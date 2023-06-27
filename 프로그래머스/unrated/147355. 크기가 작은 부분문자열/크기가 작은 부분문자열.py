def solution(t, p):
    count = 0
    for i in range(len(t)):
        if i+len(p) > len(t):
            break
        if t[i] == '0' and (len(p) > 1):
            if int(t[i+1:i+len(p)]) <= int(p):
                count+=1
        elif t[i] == '0' and (len(p) == 1):
            if int(t[i]) <= int(p):
                count+=1
        else:
            if int(t[i:i+len(p)]) <= int(p):
                count+=1
    return count