N, M = map(int,input().split())
array = []
for i in range(N):
    array.append(0)
for i in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        array[n - 1] = k
for i in range(len(array)):
    print(array[i], end =' ')