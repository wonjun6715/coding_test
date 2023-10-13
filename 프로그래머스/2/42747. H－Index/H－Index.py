def solution(citations): # citations = 피인용수
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < (i + 1): # 피인용수가 논문수보다 작아지기 시작하는 숫자가 h
            return i
    return len(citations)
