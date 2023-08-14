def solution(myStr):
    answer = []
    key = ''
    myStr += 'a'
    cnt = 0
    for i in range(len(myStr)):
        if myStr[i] == 'a' or myStr[i] == 'b' or myStr[i] == 'c':
            if key != '':
                answer.append(key)
                key = ''
                cnt += 1
        else:
            key += myStr[i]
    if cnt == 0:
        return ["EMPTY"]
    return answer