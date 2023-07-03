def solution(s):
   
    if len(s) % 2 == 1: # 홀수
        idx = len(s) // 2 + 1
        return s[idx - 1]
    else:
        idx = len(s) // 2
        return s[idx - 1] + s[idx]
        
   