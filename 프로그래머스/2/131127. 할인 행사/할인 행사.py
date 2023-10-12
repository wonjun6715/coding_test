def solution(want, number, discount):
    answer = 0
    dict_wish = {}
    for i in range(len(want)):
        dict_wish[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        dict_tmp = dict_wish.copy()
        for j in range(i, i + 10):
            if discount[j] in dict_tmp and dict_tmp[discount[j]] != 0:
                dict_tmp[discount[j]] -= 1
            else:
                break
        if sum(dict_tmp.values()) == 0:
            answer += 1
                
    return answer