def solution(before, after):
    answer = 0
    for i in range(len(before)):
        a = before.count(before[i])
        b = after.count(before[i])
        if a == b:
            continue
        else:
            return 0
    return 1