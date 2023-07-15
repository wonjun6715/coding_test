def solution(sizes):
    answer = 0
    minimum = []
    max_value = max(map(max, sizes))
    for i in sizes:
        minimum.append(min(i))
    h = max(minimum)
    return max_value * h