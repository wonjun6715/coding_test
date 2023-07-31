def solution(arr, intervals):
    answer = []
    a = (arr[intervals[0][0] : intervals[0][1] + 1])
    b = (arr[intervals[1][0] : intervals[1][1] + 1])
    return a + b