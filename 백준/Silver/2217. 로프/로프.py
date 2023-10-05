N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
a.sort(reverse=True)
answer = []
for i in range(len(a)):
    answer.append((i + 1) * a[i])

print(max(answer))