n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_ = sorted(a)
b_ = sorted(b, reverse = True)
sum = 0
for i in range(n):
    sum += (a_[i] * b_[i])
    
print(sum)
