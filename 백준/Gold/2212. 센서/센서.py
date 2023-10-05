N = int(input())
K = int(input())

answer = list(map(int, input().split()))
    
answer.sort()
if K >= N:
    print(0)
    exit()

result = []
for i in range(1, N):
    result.append(answer[i] - answer[i-1])
result.sort(reverse=True)

for i in range(K - 1):
    result.pop(0)

print(sum(result))