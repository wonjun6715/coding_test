def solution(arr):
    answer = []
    for c in arr:
        if len(answer) == 0 or answer[-1] != c: # 스택이 비어있거나, top가 push 하는 수와 다른 경우
            answer.append(c)
    return answer