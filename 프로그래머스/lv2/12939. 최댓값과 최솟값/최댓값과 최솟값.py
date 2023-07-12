def solution(s):
    answer = ''
    result = s.split() # 공백을 기준으로 리스트에 넣음
    for i in range(len(result)):
        result[i] = int(result[i])
    return f'{min(result)} {max(result)}'