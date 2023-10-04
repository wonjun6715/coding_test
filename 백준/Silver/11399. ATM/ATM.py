sum = 0
sum_ = 0
tmp = 0
n = int(input())
answer = []
answer = list(map(int, input().split()))
answer_ = sorted(answer)

for i in range(len(answer_)):
    sum_ = answer_[i] #  1 2 3
    sum += sum_ 
    tmp += sum
    
print(tmp)
