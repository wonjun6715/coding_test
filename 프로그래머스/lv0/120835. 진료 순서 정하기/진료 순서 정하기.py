def solution(emergency):
    answer = [0] * len(emergency)
    rank = 1
    result = emergency.copy()
    while len(emergency) != 0:
        answer[result.index(max(emergency))] = rank
        rank += 1
        emergency.remove(max(emergency))
    return answer