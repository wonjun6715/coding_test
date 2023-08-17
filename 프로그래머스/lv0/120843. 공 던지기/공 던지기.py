def solution(numbers, k):
    answer = 0
    length = len(numbers)
    i = 0
    cnt = 0
    pt = 0
    while True:
        pt = i % length
        i += 2
        cnt += 1
        if cnt == k:
            return numbers[pt]