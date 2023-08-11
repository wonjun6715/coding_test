def solution(s):
    answer = ''
    result = sorted(s)
    for i in result:
        if result.count(i) == 1:
            answer += i
    return answer