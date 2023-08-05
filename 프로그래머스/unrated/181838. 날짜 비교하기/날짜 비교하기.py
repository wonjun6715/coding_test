def solution(date1, date2):
    for a, b in zip(date1, date2):
        if a < b:
            return 1
        elif a == b:
            continue
        else:
            return 0
    return 0