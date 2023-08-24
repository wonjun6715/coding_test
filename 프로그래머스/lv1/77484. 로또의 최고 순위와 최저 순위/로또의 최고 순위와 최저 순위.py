def solution(lottos, win_nums):
    answer = []
    result = []
    dict_ = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    length = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            answer.append(i)
    top = len(answer) + length
    low = len(answer)
    
    for key, value in dict_.items():
        if top == key:
            result.append(value)
        if low == key:
            result.append(value)
        
    
        
    return result