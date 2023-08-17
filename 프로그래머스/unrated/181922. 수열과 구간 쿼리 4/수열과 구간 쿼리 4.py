def solution(arr, queries):
    for i in range(len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        c = queries[i][2]
        for j in range(len(arr)):
            if j >= a and j <= b and j % c == 0:
                arr[j] += 1
    return arr
            