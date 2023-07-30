import itertools
def solution(numbers):
    max = -10001 * 10000
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > max:
                max = numbers[i] * numbers[j]
    return max