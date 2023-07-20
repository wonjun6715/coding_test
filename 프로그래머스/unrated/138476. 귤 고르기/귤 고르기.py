def solution(k, tangerine):
    answer = 0
    num_dict = {}
    count = 0
    for i in tangerine:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    result = sorted(num_dict.items(), key = lambda x: x[1], reverse = True)
    for i in range(len(result)):
        answer += result[i][1]
        count += 1
        if answer >= k:
            break
            
        
    return count