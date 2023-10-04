def Euclidian(a, b):
    r = a % b
    if r == 0:
        return b
    return Euclidian(b,r)

n = int(input())
answer = []
for i in range(n):
    a, b = map(int,input().split())
    print((a * b) // Euclidian(a,b))
    