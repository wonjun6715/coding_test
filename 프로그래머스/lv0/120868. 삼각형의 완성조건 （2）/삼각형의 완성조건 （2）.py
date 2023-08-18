def solution(sides):
    answer = 0
    cnt = 0
    i = 0
    j = 0
    # 가장 큰 변의 길이가 max(sides)일 때
    tmp = max(sides) - min(sides) + 1
    while tmp + i != max(sides):
        cnt += 1
        i += 1
    # 나머지 한 변의 길이가 가장 긴 변인 경우
    tmp1 = min(sides) + max(sides) - 1
    while max(sides) + j != tmp1:
        cnt += 1
        j += 1
    
        
    return cnt + 1