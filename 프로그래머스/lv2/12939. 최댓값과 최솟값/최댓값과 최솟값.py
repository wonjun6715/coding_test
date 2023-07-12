def solution(s):
    answer = ''
    result = list(map(int, s.split()))
    return f'{min(result)} {max(result)}'